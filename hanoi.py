pegs = [[], [], []]  # Each list will hold disks, starting with peg 1 (index 0)

def initialize_pegs(n):
    """Initialize pegs for starting configuration with n disks on peg 1."""
    global pegs
    pegs = [list(range(n, 0, -1)), [], []] 
  
def print_pegs():
    """Print current state of pegs."""
    for i, peg in enumerate(pegs):
        print(f"Peg {i+1}: {peg}")
      
def hanoi_1(n, source, intermediate, destination):
    """Move disks following Variant 1 rules."""
    if n == 0:
        return
    hanoi_variant1(n-1, source, destination, intermediate)
    pegs[intermediate].append(pegs[source].pop())
    print_pegs()
    hanoi_variant1(n-1, destination, intermediate, source)
    pegs[destination].append(pegs[intermediate].pop())
    print_pegs()
    hanoi_variant1(n-1, source, destination, intermediate)


def move_clockwise(n, source, steps=1):
    if n == 0:
        return
    next_peg = (source + steps) % 3
    prev_peg = (source - 1) % 3
    move_clockwise(n-1, source, 2 if steps == 2 else 1)
    pegs[next_peg].append(pegs[source].pop())
    print_pegs()
    if steps == 2:
        move_clockwise(n-1, prev_peg, 1)  # Move n-1 disks one peg clockwise for alignment
        pegs[next_peg].append(pegs[prev_peg].pop())
        print_pegs()
        move_clockwise(n-1, source, 2) 

def hanoi_variant3(n, source, destination):
    if n <= 1:
        return
    intermediate = 3 - source - destination
    hanoi_variant1(n-2, source, destination, intermediate)
    if n > 1:
        pegs[destination].append(pegs[source].pop())
        print_pegs()
    hanoi_variant1(n-2, intermediate, source, destination)



initialize_pegs(3)  
print_pegs()
hanoi_variant1(3, 0, 1, 2)
