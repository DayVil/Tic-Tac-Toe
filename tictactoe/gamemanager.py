class Gamemanager:
    def __init__(self) -> None:
        self.__player = True

    @property
    def player(self):
        return self.__player

    def turn_player(self):
        if self.player:
            self.__player = False
        else:
            self.__player = True

    def __col_vektor(self, mat, i):
        tmp = (mat[val][i] for val in range(3))
        return tmp

    def __row_vektor(self, mat, i):
        tmp = (mat[i][val] for val in range(3))
        return tmp

    def __diag_vektor(self, mat, i):
        tmp = ()
        if i == 0:
            tmp = (mat[0][0], mat[1][1], mat[2][2])
        else:
            tmp = (mat[0][2], mat[1][1], mat[2][0])
        return tmp

    def __check_tpl(self, tpl):
        a, b, c = tpl
        if a == b == c == 1:
            return 1
        elif a == b == c == 0:
            return 0
        return -1

    def state(self, mat):
        # columns
        for i in range(3):
            val = self.__check_tpl(self.__col_vektor(mat, i))
            if 1 == val:
                return "BLUE"
            elif 0 == val:
                return "RED"

        # row
        for i in range(3):
            val = self.__check_tpl(self.__row_vektor(mat, i))
            if 1 == val:
                return "BLUE"
            elif 0 == val:
                return "RED"

        # diagonals
        for i in range(2):
            val = self.__check_tpl(self.__diag_vektor(mat, i))
            if 1 == val:
                return "BLUE"
            elif 0 == val:
                return "RED"

        if not any(-1 in sublist for sublist in mat):
            return "FULL"

        return "UNDEFINED"
