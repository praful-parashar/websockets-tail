# import fake
from faker import Faker
# import csv
import time
fake = Faker()

# with open("/Users/praful/websockets/access.log", "w") as f:
#     count = 0
#     writer = csv.writer(f)
#     while True and count < 20:
#         time.sleep(2)
#         # create the csv writer
#         print(count)
        
#         name_log = [fake.name(), fake.email(), fake.country()]
#         # write a row to the csv file
#         writer.writerow(name_log)
#         count += 1

# f.close()


import logging

#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "access.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

logger = logging.getLogger()

#Testing our Logger
# for i in range(0, 10):
while True:
    time.sleep(2)
    logger.error("Our First Log Message - {}".format(fake.name()))


# import asyncio

# async def main():
#     print("G to Y to the A to the N")
#     print('Hello ...')
#     # await asyncio.sleep(1)
#     await print_func()
#     print("nunu pawi")
#     print("deddhan")

# def print_func():
#     import time
#     # time.sleep(1)
#     # print('... World!')
#     return '------world'

# asyncio.run(main())