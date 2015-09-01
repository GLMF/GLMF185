def moveDisk(start, end):
    print('Déplacement du disque de', start, 'vers', end)

def moveTower(size, start, end, middle):
    if size == 1:
        moveDisk(start, end)
    else:
        moveTower(size - 1, start, middle, end)
        moveDisk(start, end)
        moveTower(size - 1, middle, end, start)

if __name__ == '__main__':
   moveTower(4, 'axe_gauche', 'axe_droit', 'axe_central')
