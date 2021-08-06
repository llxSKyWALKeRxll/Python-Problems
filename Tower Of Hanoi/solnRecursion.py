def towerOfHanoi(noOfDisks, startPeg=1, endPeg=3):
    if noOfDisks:
        towerOfHanoi(noOfDisks-1, startPeg, 6-startPeg-endPeg)
        print(f"Move disk {noOfDisks} from peg {startPeg} to {endPeg}")
        towerOfHanoi(noOfDisks-1, 6-startPeg-endPeg, endPeg)

if __name__=="__main__":
    print("*** TOWER OF HANOI ***")
    towerOfHanoi(noOfDisks=4)