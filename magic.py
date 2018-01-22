#-*- coding: utf-8 -*-
SIDES = (0, 1, 2, 3, 4, 5) #上 下 左 右 前 后

BLOCKCHANGE = ((5, 3, 4, 2), (2, 4, 3, 5), (0, 4, 1, 5), (5, 1, 4, 0), (0, 3, 1, 2), (2, 1, 3, 0))

# NOCOL = 0
COL1 = 0
COL2 = 1
COL3 = 2
COL4 = 3
COL5 = 4
COL6 = 5
FACES = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8),#上
    (24, 25, 26, 21, 22, 23, 18, 19, 20), #下
    (0, 3, 6, 9, 12, 15, 18, 21, 24), #左
    (8, 5, 2, 17, 14, 11, 26, 23, 20),#右
    (6, 7, 8, 15, 16, 17, 24, 25, 26), #前
    (2, 1, 0, 11, 10, 9, 20, 19, 18), #后
)
MAGICCHANGE = (
    (0, 1, 2, 2, 5, 8, 8, 7, 6, 6, 3, 0), #上
    (24, 25, 26, 26, 23, 20, 20, 19, 18, 18, 21, 24),
    (0, 3, 6, 6, 15, 24, 24, 21, 18, 18, 9, 0), #左
    (8, 5, 2, 2, 11, 20, 20, 23, 26, 26, 17, 8),
    (6, 7, 8, 8, 17, 26, 26, 25, 24, 24, 15, 6), #前
    (2, 1, 0, 0, 9, 18, 18, 19, 20, 20, 11, 2),
)

class Block(object):
    ID = 0
    def __init__(self, cols):
        self.id = Block.ID
        Block.ID += 1
        self.cols = cols
    def rotate(self, direction, bits=1):
        cols = []
        for i in BLOCKCHANGE[direction]:
            cols.append(self.cols[i])
        for i in range(4):
            index = (i + bits) % 4
            self.cols[BLOCKCHANGE[direction][index]] = cols[i]
        # for i in BLOCKCHANGE[direction]:
        #     cols.append(self.cols[i])
        # print self.id, cols

    def getCol(self, side):
        return self.cols[side]

class Magic(object):
    def __init__(self, blocks):
        self.blocks = blocks

    def __str__(self):
        str1 = ""
        sp = "                       "
        str1 += sp + "****** " + str(0) + " ******"
        for i in range(9):
            if i % 3 == 0:
                str1 += "\n" + sp
            col = self.blocks[FACES[0][i]].getCol(0)
            str1 += str(col) + "      "

        str1 += "\n\n"

        for j in [2, 4, 3, 5]:
            str1 += " ****** " + str(j) + " ******      "


        for i in range(3):
            str1 += "\n"
            for j in [2, 4, 3, 5]:
                str1 += " "
                for k in range(3):
                    col = self.blocks[FACES[j][i * 3 + k]].getCol(j)
                    str1 += str(col) + "      "

        str1 += "\n\n" + sp + "****** " + str(1) + " ******"
        for i in range(9):
            if i % 3 == 0:
                str1 += "\n" + sp
            col = self.blocks[FACES[1][i]].getCol(1)
            str1 += str(col) + "      "

        return str1

    def rotate(self, side, bits=1):
        bits %= 4
        # print FACES[side]
        for i in FACES[side]:
            self.blocks[i].rotate(side, bits)
        blocks = []
        for i in MAGICCHANGE[side]:
            blocks.append(self.blocks[i])
        # print [block.id for block in blocks]
        for i in range(12):
            index = (i + bits * 3) % 12
            self.blocks[MAGICCHANGE[side][index]] = blocks[i]
        print self

if __name__ == "__main__":
    blocks = [
        [COL1, COL2, COL3, COL4, COL5, COL6], #0
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
        [COL1, COL2, COL3, COL4, COL5, COL6],
    ]
    b = []
    for i in blocks:
        b.append(Block(i))
    m = Magic(b)
    m.rotate(1, 1)
