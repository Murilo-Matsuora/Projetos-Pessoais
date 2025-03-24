#include <stdio.h>
#include <stdlib.h>

#define MAXKEYS 3
#define MINKEYS 1
#define NIL (-1)
#define NOKEY '@'
#define NO 0
#define YES 1
typedef struct
{
    int keycount;           // number of keys in page
    char key[3];        // the actual keys
    int child[4]; // ptrs to rrns of descendants
}BTPAGE;
#define PAGESIZE sizeof(BTPAGE)

/* prototypes */
void btclose();
int btopen();
int btread(int rrn, BTPAGE *page_ptr);
int btwrite(int rrn, BTPAGE *page_ptr);
int create_root(char key, int left, int right);
int create_tree();
int getpage();
int getroot();
int insert(int rrn, char key, int *promo_r_child, char *promo_key);
void ins_in_page(char key, int r_child, BTPAGE *p_page);
void pageinit(BTPAGE *p_page);
void putroot(int root);
int search_node(char key, BTPAGE *p_page, int *pos);
void split(char key, int r_child, BTPAGE *p_oldpage, char *promo_key, int *promo_r_child, BTPAGE *p_newpage);



int main()
{

    int promoted;   // boolean: tells if a promotion from below
    int root,     // rrn of root page
        promo_rrn;  // rrn promoted from below
    char promo_key, // key promoted from below
        key = 'a';        // next key to insert in tree
    if (btopen())
    {
        root = getroot();
    }
    else
    {
        root = create_tree();
    }
    scanf(" %c",&key);
    while (key != 'q')
    {
        printf("key: %c\n", key);
        promoted = insert(root, key, &promo_rrn, &promo_key);
        if (promoted)
            root = create_root(promo_key, root, promo_rrn);
        scanf(" %c",&key);
    }
    btclose();
}

int insert(int rrn, char key, int *promo_r_child, char *promo_key)
{
    BTPAGE page,         // current page
        newpage;         // new page created if split occurs

    page.key[MAXKEYS]='\0';
    newpage.key[MAXKEYS]='\0';

    int found, promoted; // boolean values
    int pos,
        p_b_rrn;  // rrn promoted from below
    char p_b_key; // key promoted from below
    if (rrn == NIL)
    {
        *promo_key = key;
        *promo_r_child = NIL;
        return (YES);
    }
    btread(rrn, &page);
    found = search_node(key, &page, &pos);
    if (found)
    {
        printf("Error: attempt to insert duplicate key: %c \n\007", key);

        return (0);
    }
    promoted = insert(page.child[pos], key, &p_b_rrn, &p_b_key);
    if (!promoted)
    {
        return (NO);
    }
    if (page.keycount < MAXKEYS)
    {
        ins_in_page(p_b_key, p_b_rrn, &page);
        btwrite(rrn, &page);
        return (NO);
    }
    else
    {
        split(p_b_key, p_b_rrn, &page, promo_key, promo_r_child, &newpage);
        btwrite(rrn, &page);
        btwrite(*promo_r_child, &newpage);
        printf("Chave %c inserida com sucesso.\n",key);
        return (YES);
    }
}

FILE* btfd; // global file descriptor for "btree.dat"

int btopen()
{
    btfd = fopen("btree.bin", "r+b");

    if(btfd == NULL)
        return NO;
    else
        return YES;
}

void btclose()
{
    fclose(btfd);
}

int getroot()
{
    int root;
    fseek(btfd, 0, SEEK_SET);
    if (fread(&root, sizeof(int), 1, btfd) == 0)
    {
        printf("Error: Unable to get root. \007\n");
        exit(1);
    }
    return (root);
}

void putroot(int root)
{
    fseek(btfd, 0, SEEK_SET);
    fwrite(&root, sizeof(int), 1, btfd);
}

int create_tree()
{
    char key;

    btfd = fopen("btree.bin", "w+b");
    fseek(btfd, 0, SEEK_SET);
    fwrite(&(int){-1}, sizeof(int), 1, btfd);
    fclose(btfd);
    btopen();
    //key = getchar();
    scanf("%c ", &key);
    return (create_root(key, NIL, NIL));
}

int getpage()
{
    long addr;
    fseek(btfd,0,SEEK_END);
    addr = ftell(btfd) - sizeof(int);
    return ((int)addr / PAGESIZE);
}

int btread(int rrn, BTPAGE *page_ptr)
{
    long addr;
    addr = (long)rrn * (long)PAGESIZE + sizeof(int);
    fseek(btfd, addr, SEEK_SET);
    return (fread(page_ptr, sizeof(BTPAGE), 1, btfd));
}

int btwrite(int rrn, BTPAGE *page_ptr)
{
    long addr;
    addr = (long)rrn * (long)PAGESIZE + sizeof(int);
    fseek(btfd, addr, SEEK_SET);
    return (fwrite(page_ptr, sizeof(BTPAGE), 1, btfd));
}

int create_root(char key, int left, int right)
{
    BTPAGE page;

    int rrn;
    rrn = getpage();
    pageinit(&page);
    page.key[0] = key;
    page.child[0] = left;
    page.child[1] = right;
    printf("page.child[0]: %d, page.child[1]: %d\n", page.child[0], page.child[1]);

    page.keycount = 1;
    btwrite(rrn, &page);
    putroot(rrn);
    return (rrn);
}

void pageinit(BTPAGE *p_page)
{
    int j;
    for (j = 0; j < MAXKEYS; j++)
    {
        p_page->key[j] = NOKEY;
        p_page->child[j] = NIL;
    }
    p_page->child[MAXKEYS] = NIL;
}

int search_node(char key, BTPAGE *p_page, int *pos)
{
    int i;
    for (i = 0; i < p_page->keycount && key > p_page->key[i]; i++)
        printf("i: %d, p_page->keycount: %d, p_page->key[i]: %c\n", i, p_page->keycount, p_page->key[i])
        ;
    *pos = i;
    if (*pos < p_page->keycount && key == p_page->key[*pos])
    {
        return (YES);
    }
    else
    {
        return (NO);
    }
}

void ins_in_page(char key, int r_child, BTPAGE *p_page)
{
    int j;
    for (j = p_page->keycount; key < p_page->key[j - 1] && j > 0; j--)
    {
        p_page->key[j] = p_page->key[j - 1];
        p_page->child[j + 1] = p_page->child[j];
    }
    p_page->keycount++;
    p_page->key[j] = key;
    p_page->child[j + 1] = r_child;
}

void split(char key, int r_child, BTPAGE *p_oldpage, char *promo_key, int *promo_r_child, BTPAGE *p_newpage)
{
    int j;
    int mid;
    char workkeys[MAXKEYS + 1];

    int workchil[MAXKEYS + 2];
    for (j = 0; j < MAXKEYS; j++)
    {
        workkeys[j] = p_oldpage->key[j];
        workchil[j] = p_oldpage->child[j];
    }
    workchil[j] = p_oldpage->child[j];
    for (j = MAXKEYS; key < workkeys[j - 1] && j > 0; j--)
    {
        workkeys[j] = workkeys[j - 1];
        workchil[j + 1] = workchil[j];
    }
    workkeys[j] = key;
    workchil[j + 1] = r_child;
    *promo_r_child = getpage();
    pageinit(p_newpage);
    for (j = 0; j < MINKEYS; j++){
        p_oldpage->key[j] = workkeys[j];
        p_oldpage->child[j] = workchil[j];
        p_newpage->key[j] = workkeys[j+2+MINKEYS];
        p_newpage->child[j] = workchil[j+2+MINKEYS];
        p_oldpage->key[j+1+MINKEYS] = NOKEY;
        p_oldpage->child[j+2+MINKEYS] = NIL;
    }
    p_oldpage->child[MINKEYS] = workchil[MINKEYS];
    p_oldpage->child[MINKEYS+1] = workchil[MINKEYS+1];
    p_newpage->child[MINKEYS] = workchil[j+2+MINKEYS];

    p_newpage->keycount = MINKEYS;
    p_oldpage->keycount = MAXKEYS - MINKEYS;
    *promo_key = workkeys[MINKEYS+1];

    printf("Divisão de nó.\nChave %c promovida.",*promo_key);
}