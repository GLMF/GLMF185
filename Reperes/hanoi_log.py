def moveDisk(start, end):
    print('=> moveDisk(start={}, end={})'.format(start, end))

def moveTower(size, start, end, middle):
    if size == 1:
        moveDisk(start, end)
    else:
        print('[A] moveTower(size={}, start={}, end={}, middle={})'
              .format(size - 1, start, middle, end))
        moveTower(size - 1, start, middle, end)
        moveDisk(start, end)
        print('[R] moveTower(size={}, start={}, end={}, middle={})'
              .format(size - 1, middle, end, start))
        moveTower(size - 1, middle, end, start)

if __name__ == '__main__':
    print('[S] moveTower(size=4, start=axe_gauche, end=axe_droit, ' +
          'middle=axe_central)')
    moveTower(4, 'axe_gauche', 'axe_droit', 'axe_central')
