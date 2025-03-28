def towers_of_hanoi(nro_disks, from_tower=1, to_tower=3, tmp_tower=2):
    if nro_disks == 1:
        print(f"Mover el disco {nro_disks} desde la torre {from_tower} a la torre {to_tower}")
        return
    
    towers_of_hanoi(nro_disks - 1, from_tower, tmp_tower, to_tower)

    print(f"Mover el disco {nro_disks} desde la torre {from_tower} a la torre {to_tower}")
    towers_of_hanoi(nro_disks - 1, tmp_tower, to_tower, from_tower)

if __name__ == "__main__":
    towers_of_hanoi(3)  # Defino la cantidad de discos
