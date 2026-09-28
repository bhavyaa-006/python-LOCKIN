import asyncio
import random
c = [    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
]

async def main():
    return await asyncio.gather(
        ran(1,9),
        ran(2,8),
        ran(3,7)
    )

async def ran(min,max):
    color = list(c)
    print(f"{color}INITIATED RANDOM({min}).")
    while (num := random.randint(0,len(color)-1)) <=max:
        print(f"{color}RANDOM({min})== {num} too low , retrying..." )
        await asyncio.sleep(min)
    print(f"c{color}--->: FINISHED RANDOM ({min}) == {num}"+c[0])
    return num
if __name__ == "__main__":
    random.seed(420)
    r1,r2,r3 = asyncio.run(main())
    print()
    print(f"r1 = {r1} , r2 = {r2} , r3 = {r3}")