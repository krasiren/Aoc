class Directory:
    def __init__(self, parent=None):
        self.size = 0
        self.subDirs = []
        self.parent = parent

    # We completely ignore commands all '$ cd' and '$ ls', because the input file
    # is build so that is lists each directory exactly once.
    # Then also the names of directories and file names don't matter
    def makeSubTrees(self, ix: int, lines: list[str]) -> tuple[int, int]:
        """
        Returns a tree-like structure that represents the directory hierarchically.
        Each object: (Directory) has a size: (int) and a subDirs: (list[Directory]),
        that represent child nodes in the tree(or sub directories).
        """
        while ix < len(lines) and lines[ix][0] != '$':
            if lines[ix][0].isnumeric():
                self.size += int(lines[ix].split(' ')[0])
            else:
                self.subDirs.append(Directory(self))
            ix += 1

        dir: Directory
        for dir in self.subDirs:
            ix, size = dir.makeSubTrees(ix+2, lines)
            self.size += size

        return ix+1, self.size

    def sumDirsSmallerOrEqualThan(self, size: int) -> int:
        sum = 0
        dir: Directory
        for dir in self.subDirs:
            sum += dir.sumDirsSmallerOrEqualThan(size)

        if self.size <= size:
            sum += self.size

        return sum

    # the size to delete must be bigger than lowerThreshold, but still the smallest possible
    def findSmallestDirToDelete(self, currentMinimum: int, lowerThreshold: int) -> int:
        if self.size >= lowerThreshold and self.size < currentMinimum:
            currentMinimum = self.size
        dir: Directory
        for dir in self.subDirs:
            currentMinimum = dir.findSmallestDirToDelete(
                currentMinimum, lowerThreshold)

        return currentMinimum


def first(rootDir: Directory, limit: int) -> None:
    sum = rootDir.sumDirsSmallerOrEqualThan(limit)
    print(sum)


def second(rootDir: Directory, maximumDiskSpace: int, requiredSpace: int) -> None:
    # spaceToFree = required - unused
    spaceToFree = requiredSpace - (maximumDiskSpace - rootDir.size)
    sizeOfDirToDelete = rootDir.findSmallestDirToDelete(
        rootDir.size, spaceToFree)
    print(sizeOfDirToDelete)


if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    # make a hierarchy tree of directories from input
    rootDir = Directory()
    rootDir.makeSubTrees(2, lines)

    first(rootDir, 100000)
    second(rootDir, 70000000, 30000000)
