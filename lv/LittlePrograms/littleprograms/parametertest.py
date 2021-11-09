def verzinse(betrag : float, jahre :int  = 1, zinsen : float = 0.01):
    print(f'{betrag}, {jahre}, {zinsen}')

if __name__ == '__main__':
    verzinse(1000)
    verzinse(1000, 3)
    verzinse(1000, zinsen=0.4, jahre=10)
    verzinse(betrag=1000, zinsen=0.3)

    # was geht nicht
    #verzinse(betrag=1000, 0.3, 5)
    #verzinse(wert=1000)
    #verzinse(zinsen=0.2, jahre=5)