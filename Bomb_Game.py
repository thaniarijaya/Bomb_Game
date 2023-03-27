# PROYEK STRUKTUR DATA - Kel 23
# Judul Proyek: Flinch
# Anggota Kelompok:
    # Grace Natasha - C14200021 - SD(A)
    # Ariella Thania Rijaya - C14200158 - SD(A)
    # Melissa Chaterine - C14200162 - SD(B)

import random
import os

# menghapus console - T
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# Node Linkedlist - G
class Node:
    def __init__(self, data):
        self.cover = None  # tampilan awal dari setiap node
        self.data = data  # isi sebenarnya dari node tsb, antara BOM / POIN

        # pointer
        self.right = None
        self.down = None
        self.prev = None

#Fitur tambahan saat presentasi
class History:
    def __init__(self):
        self.head = None
    
    def addNew(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            currentNode = self.head
            while(currentNode.right is not None):
                currentNode = currentNode.right
            currentNode.right = Node(data)

    def displayHistory(self):
        if self.head is not None:
            currentNode = self.head
            while (currentNode is not None):
                print(currentNode.data, end=" ")
                currentNode = currentNode.right
        else:
            print('No points yet!')




#Leaderboard - M
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Leaderboard:
    def __init__(self):
        self.list = []

    def addPlayer(self, newname, newscore):  # menambahkan data player kedalam leaderboard
        self.list.append(Player(newname, newscore))

    def sortData(self):
        # mengurutkan data player berdasarkan skor tertinggi
        self.list.sort(key=lambda x: x.score, reverse=True)
        self.removeB()
        print()

    def showLB(self):  # menampilkan data leaderboard game
        print("======= LEADERBOARD ======")
        if len(self.list) == 0:
            print("NO PLAYER RECORDS WERE FOUND !!")
        else:
            self.sortData()
            for i in range(len(self.list)):
                print(i+1, "Name : " + self.list[i].name, end=' ')
                print("\tScore : ", self.list[i].score)

    def removeB(self):  # fungsi untuk membuang data player diluar 10 orang dengan skor tertinggi dari leaderboard jika jumlahnya lebih dari 10 orang
        if len(self.list) > 10:
            while len(self.list) > 10:
                self.list.pop()


#Membuat map game dalam bentuk linkedlist - G
def make(maxCol, maxRow, bomb):
    # membuat head (posisi 0,0)
    if 0 in bomb:
        head = Node('X')
    else:
        head = Node(random.randint(10, 50))
    head.cover = '0'

    # loop utk membuat baris sebanyak jumlah baris yg diinginkan
    row = head
    for i in range(maxRow):
        col = row
        # loop utk membuat kolom sebanyak jumlah kolom yg diinginkan utk setiap baris
        for j in range(maxCol - 1):
            if (i*maxRow + j + 1) in bomb:
                col.right = Node('X')
            else:
                col.right = Node(random.randint(10, 50))
            col.right.prev = col
            col.right.cover = '0'
            col = col.right

        # semua baris diberikan node pada pointer down nya kecuali baris terakhir
        if i + 1 < maxRow:
            if ((i+1)*maxRow) in bomb:
                row.down = Node('X')
            else:
                row.down = Node(random.randint(10, 50))
            row.down.cover = '0'
            row = row.down

    return head

# untuk menghitung jumlah maksimum poin yg bisa didapatkan di level tsb (utk menentukan WIN) - G
def maxPoints(head):
    max = 0
    currentRow = head

    # loop kebawah sampai node.down = None
    while (currentRow):
        currentCol = currentRow

        # loop kesamping sampai node.right = None
        while(currentCol):
            if not currentCol.data == 'X' and not currentCol.data == 'S':
                max += int(currentCol.data)
            currentCol = currentCol.right
        currentRow = currentRow.down

    return max

# memperbesar linkedlist utk level" berikutnya - G
def appendList(head, newCol, newRow, bomb):
    # utk posisi pertama
    currentRow = head
    currentRow.cover = '0'
    if 0 in bomb:
        currentRow.data = 'X'  # diisi bomb
    else:
        currentRow.data = random.randint(10, 50)  # diisi poin

    # mulai loop utk posisi" berikutnya
    for row in range(newRow):

        currentCol = currentRow
        for col in range(newCol-1):

            if currentCol.right is None:
                if (row*newRow + col+1) in bomb:
                    currentCol.right = Node('X')  # diisi bomb
                else:
                    currentCol.right = Node(
                        random.randint(10, 50))  # diisi poin
            else:
                if (row*newRow + col+1) in bomb:
                    currentCol.right.data = 'X'  # diisi bomb
                else:
                    currentCol.right.data = random.randint(10, 50)  # diisi poin

            currentCol.right.cover = '0'
            currentCol.right.prev = currentCol
            currentCol = currentCol.right

        if row + 1 < newRow:  # kalau akan melebihi max jumlah row, jgn ditambah
            if currentRow.down is None:
                if ((row+1)*newRow) in bomb:
                    currentRow.down = Node('X')  # diisi bomb
                else:
                    currentRow.down = Node(
                        random.randint(10, 50))  # diisi poin
            else:
                if ((row+1)*newRow) in bomb:
                    currentRow.down.data = 'X'  # diisi bomb
                else:
                    currentRow.down.data = random.randint(10, 50)  # diisi poin
            currentRow.down.cover = '0'
            currentRow = currentRow.down


def display(head):  # T
    currentRow = head

    while (currentRow):
        currentCol = currentRow

        while(currentCol):
            print(currentCol.cover, end=" ")  # print bagian depannya
            currentCol = currentCol.right

        print()
        currentRow = currentRow.down


def getData(head, idxRow, idxCol):  # T
    currentRow = head
    countCol = 0
    countRow = 0
    while (currentRow):
        countRow = countRow + 1
        currentCol = currentRow
        countCol = 0
        while(currentCol):
            countCol = countCol + 1
            if(countCol == idxCol):
                break
            currentCol = currentCol.right
        if(countRow == idxRow):
            break
        currentRow = currentRow.down
    return currentCol.data


def opened(head, idxRow, idxCol):  # mengubah cover node yg sudah dipilih menjadi data aslinya - G
    currentRow = head
    countCol = 0
    countRow = 0
    while (currentRow):
        countRow = countRow + 1
        currentCol = currentRow
        countCol = 0
        while(currentCol):
            countCol = countCol + 1
            if(countCol == idxCol):
                break
            currentCol = currentCol.right
        if(countRow == idxRow):
            break
        currentRow = currentRow.down

    currentCol.cover = currentCol.data


# menghanguskan kotak sebelum dan/atau sesudah bom ketika bom dibuka - T
def openedBeforeNext(head, idxRow, idxCol):
    # index 0 buat menyimpan jumlah ke kiri, 1 ke kanan, 2 menyimpan jumlah bom yang ikut terbuka
    count = [0, 0, 0]
    currentRow = head
    countCol = 0
    countRow = 0
    while (currentRow):
        countRow = countRow + 1
        currentCol = currentRow
        countCol = 0
        while(currentCol):
            countCol = countCol + 1
            if(countCol == idxCol):
                break
            currentCol = currentCol.right
        if(countRow == idxRow):
            break
        currentRow = currentRow.down

    curr = currentCol.prev
    while curr is not None and curr.data == 'X':
        # membuka bom
        if(curr.cover != curr.data):
            curr.cover = 'X'
            count[2] = count[2] + 1
        count[0] = count[0] + 1
        curr = curr.prev
    if (curr is not None):
        # kalau belum dibuka baru diganti S (hangus)
        if(curr.cover != curr.data):
            curr.cover = 'S'
            curr.data = 'S'
        count[0] = count[0] + 1

    curr = currentCol.right
    while curr is not None and curr.data == 'X':
        # membuka bom
        if(curr.cover != curr.data):
            curr.cover = 'X'
            count[2] = count[2] + 1
        count[1] = count[1] + 1
        curr = curr.right
    if (curr is not None):
        # kalau belum dibuka baru diganti S (hangus)
        if(curr.cover != curr.data):
            curr.cover = 'S'
            curr.data = 'S'
        count[1] = count[1] + 1

    return count


def randomIdx(maxCount, row, col):  # utk merandom posisi bom - T
    idx = []
    for i in range(maxCount):
        x = random.randint(0, (row*col)-1)
        while x in idx:
            x = random.randint(0, (row*col)-1)
        idx.append(x)
    return idx


if __name__ == '__main__':

    # T

    lb = Leaderboard()
    pilih = 0
    win = False
    level = 1
    tmplist = []
    gameOver = False
    tmpscore = 0

    while pilih != 3:
        nyawa = 8

        if win == False:
            pilih = chr(pilih)
            # untuk pilihan menu pertama
            if(gameOver is False):
                print("MENU")
                print("1. Start")
                print("2. Show Leaderboard")
                print("3. Exit")
                print()

                # error handling jika user input di luar angka atau panjang inputan lebih dari 1 atau kurang dari 1
                while len(pilih) == 0 or len(pilih) > 1 or ord(pilih[0]) < 48 or ord(pilih[0]) > 57:
                    print("Pilihan : ", end="")
                    pilih = str(input())
                    if(len(pilih) == 0 or len(pilih) > 1 or ord(pilih[0]) < 48 or ord(pilih[0]) > 57):
                        print("Input tidak sesuai!")

            # untuk pilihan menu ketika game over
            else:
                print("MENU")
                print("1. New Game")
                print("2. Show Leaderboard")
                print("3. Exit")
                print()
                while len(pilih) == 0 or len(pilih) > 1 or ord(pilih[0]) < 48 or ord(pilih[0]) > 57:
                    print("Pilihan : ", end="")
                    pilih = str(input())
                    if(len(pilih) == 0 or len(pilih) > 1 or ord(pilih[0]) < 48 or ord(pilih[0]) > 57):
                        print("Input tidak sesuai!")

            pilih = int(pilih)
            if pilih == 1:
                level = 1
            clearConsole()

        if(pilih == 1):
            historyPoin = History()
            tmplist.clear()

            if level == 1:  # nama hanya diminta kalo level 1, selain itu langsung akumulasi
                tmplist.clear()
                print("=== INPUT PLAYER ===")
                name = input("Input player name : ")
                score = 0
                tmpscore = 0

            clearConsole()

            # merandom bom
            row = 3*level
            col = 3*level
            count = 0

            # jumlah bom
            maxCount = 3*level

            # merandom index utk bom
            bomb = randomIdx(maxCount, row, col)

    # G

            if level == 1:  # map game hanya di generate di level pertama
                linkedlist = make(row, col, bomb)
            else:  # selain level 1, map yang ada diappend sehingga bertambah besar
                appendList(linkedlist, col, row, bomb)

            # maximum point yg bisa dicapai dalam 1 level game
            maxPoint = maxPoints(linkedlist) + tmpscore

    # M

            # masuk ke game
            print('Level : ', level)
            win = False  # setiap mulai level baru, win diset False lagi
            while (nyawa != 0 and win == False):
                print("Current Score : ", score,
                      " || Current Life : ", nyawa)
                print()

                display(linkedlist)

                print("Pada round ini masukkan angka baris dan kolom antara 1 -", row)

    # T

                # jika user memasukkan di luar angka
                pilBaris = 'baris'
                while len(pilBaris) > len(str(row)) or len(pilBaris) < len(str(row)) or ord(pilBaris[0]) < 48 or ord(pilBaris[0]) > 57:
                    print("Baris : ", end="")
                    pilBaris = str(input())
                    if(len(pilBaris) > len(str(row)) or len(pilBaris) < len(str(row)) or ord(pilBaris[0]) < 48 or ord(pilBaris[0]) > 57):
                        print('Masukkan hanya angka saja!')
                pilBaris = int(pilBaris)

                # mengulang apabila pengguna memasukkan angka lebih besar dari jumlah baris
                while pilBaris > row or pilBaris <= 0:
                    print("Baris : ", end="")
                    pilBaris = int(input())
                    if(pilBaris > row or pilBaris <= 0):
                        print('Pastikan jumlah baris sesuai!')

                # jika user memasukkan di luar angka
                pilKolom = 'kolom'
                while len(pilKolom) < len(str(col)) or len(pilKolom) > len(str(col)) or ord(pilKolom[0]) < 48 or ord(pilKolom[0]) > 57:
                    print("Kolom : ", end="")
                    pilKolom = str(input())
                    if(len(pilKolom) < len(str(col)) or len(pilKolom) > len(str(col)) or ord(pilKolom[0]) < 48 or ord(pilKolom[0]) > 57):
                        print('Masukkan hanya angka saja!')
                pilKolom = int(pilKolom)

                # mengulang apabila pengguna memasukkan angka lebih besar dari jumlah kolom
                while pilKolom > col or pilKolom <= 0:
                    print("Kolom : ", end="")
                    pilKolom = int(input())
                    if(pilKolom > col or pilKolom <= 0):
                        print('Pastikan jumlah kolom sesuai!')
                # tmp dalam string agar mudah dilakukan pengecekan
                tmp = str(pilBaris) + str(pilKolom)

    # M - checking apabila kolom dan baris yang diinput sudah pernah dibuka atau belum
                while tmp in tmplist:  # selama data kolom baris sudah ada di tmplist, akan diminta input ulang
                    print(
                        'Baris dan kolom sudah dibuka ! Input ulang baris dan kolom lainnya !\n')
                    print("Baris : ", end="")
                    pilBaris = int(input())
                    while pilBaris > row:
                        print("Baris : ", end="")
                        pilBaris = int(input())
                    print("Kolom : ", end="")
                    pilKolom = int(input())
                    while pilKolom > col:
                        print("Kolom : ", end="")
                        pilKolom = int(input())
                    tmp = str(pilBaris) + str(pilKolom)
                else:  # jika tidak ada dalam tmplist berarti belum pernah baris & kolom blm pernah dibuka
                    tmplist.append(tmp)

                clearConsole()

    # T

                # cek apakah mendapat bom atau tidak
                isiKotak = getData(linkedlist, pilBaris, pilKolom)
                if(isiKotak == 'X'):  # bom
                    count = openedBeforeNext(linkedlist, pilBaris, pilKolom)
                    tmpKolom1 = pilKolom - 1
                    tmpKolom2 = pilKolom + 1
                    for i in range(count[0]):
                        tmp = str(pilBaris) + str(tmpKolom1)
                        tmplist.append(tmp)
                        tmpKolom1 = tmpKolom1 - 1
                    for i in range(count[1]):
                        tmp = str(pilBaris) + str(tmpKolom2)
                        tmplist.append(tmp)
                        tmpKolom2 = tmpKolom2 + 1
                    # poin maksimal dikurangi yang sudah hangus
                    nyawa = nyawa - count[2]
                    maxPoint = maxPoints(linkedlist) + tmpscore
                    print(
                        "Maaf anda mendapat bom, sehingga kotak sebelum dan/atau sesudah yang belum terbuka akan hangus dan nyawa berkurang 1")
                    nyawa -= 1
                else:
                    score += isiKotak  # poin
                    print("AMAN ! +", isiKotak, " poin")

                    #history poin
                    historyPoin.addNew(isiKotak) 
                    historyPoin.displayHistory()
                    print()

                opened(linkedlist, pilBaris, pilKolom)

    # M

                if score == maxPoint:
                    win = True

            if nyawa == 0:
                gameOver = True
                print("GAME OVER !")
                lb.addPlayer(name, int(score))

    # G

            elif score == maxPoint:
                #tmpscore = tampungan score dari level" sblmnya
                tmpscore = tmpscore + score
                win = True

                print('YOU WIN !!!')
                print("Current Score : ", score,
                      " || Current Life : ", nyawa)
                print('1. Continue to Next Level')
                print('2. Exit')
                print()
                choice = input('Pilihan: ')
                while len(choice) == 0 or len(choice) > 1 or ord(choice[0]) < 48 or ord(choice[0]) > 57:
                    choice = input('Pilihan: ')
                    if(len(choice) == 0 or len(choice) > 1 or ord(choice[0]) < 48 or ord(choice[0]) > 57):
                        print("Input tidak sesuai!")

                choice = int(choice)
                tmplist.clear()  # clear riwayat baris kolom yang sudah dibuka
                if choice == 1:
                    # naik level
                    level += 1
                    pilih = 1
                    print('-----------------')
                else:
                    lb.addPlayer(name, int(score))
                    lb.showLB()
                    print()
                    win = False
                    gameOver = True

    # M

        elif(pilih == 2):
            lb.showLB()
            print()

        elif(pilih == 3):
            tmplist.clear()
            break

        else:
            print('Pastikan pilihan menu sudah sesuai!')
            print()
