import os
import time
import pygame
from pygame.locals import *
import random


cont = 0
grafo = {(0,0): [      (1,0),(0,1)],
       	 (0,1): [      (0,0),(1,1),(0,2)],
	 (0,2): [      (0,1),(1,2),(0,3)],
	 (0,3): [      (0,2),(1,3),(0,4)],
	 (0,4): [      (0,3),(1,4),(0,5)],
	 (0,5): [      (0,4),(1,5),(0,6)],
	 (0,6): [      (0,5),(1,6),(0,7)],
	 (0,7): [      (0,6),(1,7),(0,8)],
	 (0,8): [      (0,7),(1,8),(0,9)],
	 (0,9): [      (0,8),(1,9),(0,10)],
	 (0,10): [      (0,9),(1,10),(0,11)],
	 (0,11): [      (0,10),(1,11),(0,12)],
	 (0,12): [      (0,11),(1,12),(0,13)],
	 (0,13): [      (0,12),(1,13),(0,14)],
	 (0,14): [      (0,13),(1,14),(0,15)],
	 (0,15): [      (0,14),(1,15),(0,16)],
	 (0,16): [      (0,15),(1,16),(0,17)],
	 (0,17): [      (0,16),(1,17),(0,18)],
	 (0,18): [      (0,17),(1,18),(0,19)],
	 (0,19): [      (0,18),(1,19)],

         (1,0): [(0,0),      (2,0),(1,1)],
       	 (1,1): [(0,1),(1,0),(2,1),(1,2)],
	 (1,2): [(0,2),(1,1),(2,2),(1,3)],
	 (1,3): [(0,3),(1,2),(2,3),(1,4)],
	 (1,4): [(0,4),(1,3),(2,4),(1,5)],
	 (1,5): [(0,5),(1,4),(2,5),(1,6)],
	 (1,6): [(0,6),(1,5),(2,6),(1,7)],
	 (1,7): [(0,7),(1,6),(2,7),(1,8)],
	 (1,8): [(0,8),(1,7),(2,8),(1,9)],
	 (1,9): [(0,9),(1,8),(2,9),(1,10)],
	 (1,10): [(0,10),(1,9),(2,10),(1,11)],
	 (1,11): [(0,11),(1,10),(2,11),(1,12)],
	 (1,12): [(0,12),(1,11),(2,12),(1,13)],
	 (1,13): [(0,13),(1,12),(2,13),(1,14)],
	 (1,14): [(0,14),(1,13),(2,14),(1,15)],
	 (1,15): [(0,15),(1,14),(2,15),(1,16)],
	 (1,16): [(0,16),(1,15),(2,16),(1,17)],
	 (1,17): [(0,17),(1,16),(2,17),(1,18)],
	 (1,18): [(0,18),(1,17),(2,18),(1,19)],
	 (1,19): [(0,19),(1,18),(2,19)],

         (2,0): [(1,0),     (3,0),(2,1)],
       	 (2,1): [(1,1),(2,0),(3,1),(2,2)],
	 (2,2): [(1,2),(2,1),(3,2),(2,3)],
	 (2,3): [(1,3),(2,2),(3,3),(2,4)],
	 (2,4): [(1,4),(2,3),(3,4),(2,5)],
	 (2,5): [(1,5),(2,4),(3,5),(2,6)],
	 (2,6): [(1,6),(2,5),(3,6),(2,7)],
	 (2,7): [(1,7),(2,6),(3,7),(2,8)],
	 (2,8): [(1,8),(2,7),(3,8),(2,9)],
	 (2,9): [(1,9),(2,8),(3,9),(2,10)],
	 (2,10): [(1,10),(2,9),(3,10),(2,11)],
	 (2,11): [(1,11),(2,10),(3,11),(2,12)],
	 (2,12): [(1,12),(2,11),(3,12),(2,13)],
	 (2,13): [(1,13),(2,12),(3,13),(2,14)],
	 (2,14): [(1,14),(2,13),(3,14),(2,15)],
	 (2,15): [(1,15),(2,14),(3,15),(2,16)],
	 (2,16): [(1,16),(2,15),(3,16),(2,17)],
	 (2,17): [(1,17),(2,16),(3,17),(2,18)],
	 (2,18): [(1,18),(2,17),(3,18),(2,19)],
	 (2,19): [(1,19),(2,18),(3,19)],

         (3,0): [(2,0),      (4,0),(3,1)],
       	 (3,1): [(2,1),(3,0),(4,1),(3,2)],
	 (3,2): [(2,2),(3,1),(4,2),(3,3)],
	 (3,3): [(2,3),(3,2),(4,3),(3,4)],
	 (3,4): [(2,4),(3,3),(4,4),(3,5)],
	 (3,5): [(2,5),(3,4),(4,5),(3,6)],
	 (3,6): [(2,6),(3,5),(4,6),(3,7)],
	 (3,7): [(2,7),(3,6),(4,7),(3,8)],
	 (3,8): [(2,8),(3,7),(4,8),(3,9)],
	 (3,9): [(2,9),(3,8),(4,9),(3,10)],
	 (3,10): [(2,10),(3,9),(4,10),(3,11)],
	 (3,11): [(2,11),(3,10),(4,11),(3,12)],
	 (3,12): [(2,12),(3,11),(4,12),(3,13)],
	 (3,13): [(2,13),(3,12),(4,13),(3,14)],
	 (3,14): [(2,14),(3,13),(4,14),(3,15)],
	 (3,15): [(2,15),(3,14),(4,15),(3,16)],
	 (3,16): [(2,16),(3,15),(4,16),(3,17)],
	 (3,17): [(2,17),(3,16),(4,17),(3,18)],
	 (3,18): [(2,18),(3,17),(4,18),(3,19)],
	 (3,19): [(2,19),(3,18),(4,19)],

	 (4,0): [(3,0),      (5,0),(4,1)],
       	 (4,1): [(3,1),(4,0),(5,1),(4,2)],
	 (4,2): [(3,2),(4,1),(5,2),(4,3)],
	 (4,3): [(3,3),(4,2),(5,3),(4,4)],
	 (4,4): [(3,4),(4,3),(5,4),(4,5)],
	 (4,5): [(3,5),(4,4),(5,5),(4,6)],
	 (4,6): [(3,6),(4,5),(5,6),(4,7)],
	 (4,7): [(3,7),(4,6),(5,7),(4,8)],
	 (4,8): [(3,8),(4,7),(5,8),(4,9)],
	 (4,9): [(3,9),(4,8),(5,9),(4,10)],
	 (4,10): [(3,10),(4,9),(5,10),(4,11)],
	 (4,11): [(3,11),(4,10),(5,11),(4,12)],
	 (4,12): [(3,12),(4,11),(5,12),(4,13)],
	 (4,13): [(3,13),(4,12),(5,13),(4,14)],
	 (4,14): [(3,14),(4,13),(5,14),(4,15)],
	 (4,15): [(3,15),(4,14),(5,15),(4,16)],
	 (4,16): [(3,16),(4,15),(5,16),(4,17)],
	 (4,17): [(3,17),(4,16),(5,17),(4,18)],
	 (4,18): [(3,18),(4,17),(5,18),(4,19)],
	 (4,19): [(3,19),(4,18),(5,19)],

	 (5,0): [(4,0),      (6,0),(5,1)],
       	 (5,1): [(4,1),(5,0),(6,1),(5,2)],
	 (5,2): [(4,2),(5,1),(6,2),(5,3)],
	 (5,3): [(4,3),(5,2),(6,3),(5,4)],
	 (5,4): [(4,4),(5,3),(6,4),(5,5)],
	 (5,5): [(4,5),(5,4),(6,5),(5,6)],
	 (5,6): [(4,6),(5,5),(6,6),(5,7)],
	 (5,7): [(4,7),(5,6),(6,7),(5,8)],
	 (5,8): [(4,8),(5,7),(6,8),(5,9)],
	 (5,9): [(4,9),(5,8),(6,9),(5,10)],
	 (5,10): [(4,10),(5,9),(6,10),(5,11)],
	 (5,11): [(4,11),(5,10),(6,11),(5,12)],
	 (5,12): [(4,12),(5,11),(6,12),(5,13)],
	 (5,13): [(4,13),(5,12),(6,13),(5,14)],
	 (5,14): [(4,14),(5,13),(6,14),(5,15)],
	 (5,15): [(4,15),(5,14),(6,15),(5,16)],
	 (5,16): [(4,16),(5,15),(6,16),(5,17)],
	 (5,17): [(4,17),(5,16),(6,17),(5,18)],
	 (5,18): [(4,18),(5,17),(6,18),(5,19)],
	 (5,19): [(4,19),(5,18),(6,19)],

         (6,0): [(5,0),      (7,0),(6,1)],
       	 (6,1): [(5,1),(6,0),(7,1),(6,2)],
	 (6,2): [(5,2),(6,1),(7,2),(6,3)],
	 (6,3): [(5,3),(6,2),(7,3),(6,4)],
	 (6,4): [(5,4),(6,3),(7,4),(6,5)],
	 (6,5): [(5,5),(6,4),(7,5),(6,6)],
	 (6,6): [(5,6),(6,5),(7,6),(6,7)],
	 (6,7): [(5,7),(6,6),(7,7),(6,8)],
	 (6,8): [(5,8),(6,7),(7,8),(6,9)],
	 (6,9): [(5,9),(6,8),(7,9),(6,10)],
	 (6,10): [(5,10),(6,9),(7,10),(6,11)],
	 (6,11): [(5,11),(6,10),(7,11),(6,12)],
	 (6,12): [(5,12),(6,11),(7,12),(6,13)],
	 (6,13): [(5,13),(6,12),(7,13),(6,14)],
	 (6,14): [(5,14),(6,13),(7,14),(6,15)],
	 (6,15): [(5,15),(6,14),(7,15),(6,16)],
	 (6,16): [(5,16),(6,15),(7,16),(6,17)],
	 (6,17): [(5,17),(6,16),(7,17),(6,18)],
	 (6,18): [(5,18),(6,17),(7,18),(6,19)],
	 (6,19): [(5,19),(6,18),(7,19)],

         (7,0): [(6,0),      (8,0),(7,1)],
       	 (7,1): [(6,1),(7,0),(8,1),(7,2)],
	 (7,2): [(6,2),(7,1),(8,2),(7,3)],
	 (7,3): [(6,3),(7,2),(8,3),(7,4)],
	 (7,4): [(6,4),(7,3),(8,4),(7,5)],
	 (7,5): [(6,5),(7,4),(8,5),(7,6)],
	 (7,6): [(6,6),(7,5),(8,6),(7,7)],
	 (7,7): [(6,7),(7,6),(8,7),(7,8)],
	 (7,8): [(6,8),(7,7),(8,8),(7,9)],
	 (7,9): [(6,9),(7,8),(8,9),(7,10)],
	 (7,10): [(6,10),(7,9),(8,10),(7,11)],
	 (7,11): [(6,11),(7,10),(8,11),(7,12)],
	 (7,12): [(6,12),(7,11),(8,12),(7,13)],
	 (7,13): [(6,13),(7,12),(8,13),(7,14)],
	 (7,14): [(6,14),(7,13),(8,14),(7,15)],
	 (7,15): [(6,15),(7,14),(8,15),(7,16)],
	 (7,16): [(6,16),(7,15),(8,16),(7,17)],
	 (7,17): [(6,17),(7,16),(8,17),(7,18)],
	 (7,18): [(6,18),(7,17),(8,18),(7,19)],
	 (7,19): [(6,19),(7,18),(8,19)],

         (8,0): [(7,0),      (9,0),(8,1)],
       	 (8,1): [(7,1),(8,0),(9,1),(8,2)],
	 (8,2): [(7,2),(8,1),(9,2),(8,3)],
	 (8,3): [(7,3),(8,2),(9,3),(8,4)],
	 (8,4): [(7,4),(8,3),(9,4),(8,5)],
	 (8,5): [(7,5),(8,4),(9,5),(8,6)],
	 (8,6): [(7,6),(8,5),(9,6),(8,7)],
	 (8,7): [(7,7),(8,6),(9,7),(8,8)],
	 (8,8): [(7,8),(8,7),(9,8),(8,9)],
	 (8,9): [(7,9),(8,8),(9,9),(8,10)],
	 (8,10): [(7,10),(8,9),(9,10),(8,11)],
	 (8,11): [(7,11),(8,10),(9,11),(8,12)],
	 (8,12): [(7,12),(8,11),(9,12),(8,13)],
	 (8,13): [(7,13),(8,12),(9,13),(8,14)],
	 (8,14): [(7,14),(8,13),(9,14),(8,15)],
	 (8,15): [(7,15),(8,14),(9,15),(8,16)],
	 (8,16): [(7,16),(8,15),(9,16),(8,17)],
	 (8,17): [(7,17),(8,16),(9,17),(8,18)],
	 (8,18): [(7,18),(8,17),(9,18),(8,19)],
	 (8,19): [(7,19),(8,18),(9,19)],

         (9,0): [(8,0),      (10,0),(9,1)],
       	 (9,1): [(8,1),(9,0),(10,1),(9,2)],
	 (9,2): [(8,2),(9,1),(10,2),(9,3)],
	 (9,3): [(8,3),(9,2),(10,3),(9,4)],
	 (9,4): [(8,4),(9,3),(10,4),(9,5)],
	 (9,5): [(8,5),(9,4),(10,5),(9,6)],
	 (9,6): [(8,6),(9,5),(10,6),(9,7)],
	 (9,7): [(8,7),(9,6),(10,7),(9,8)],
	 (9,8): [(8,8),(9,7),(10,8),(9,9)],
	 (9,9): [(8,9),(9,8),(10,9),(9,10)],
	 (9,10): [(8,10),(9,9),(10,10),(9,11)],
	 (9,11): [(8,11),(9,10),(10,11),(9,12)],
	 (9,12): [(8,12),(9,11),(10,12),(9,13)],
	 (9,13): [(8,13),(9,12),(10,13),(9,14)],
	 (9,14): [(8,14),(9,13),(10,14),(9,15)],
	 (9,15): [(8,15),(9,14),(10,15),(9,16)],
	 (9,16): [(8,16),(9,15),(10,16),(9,17)],
	 (9,17): [(8,17),(9,16),(10,17),(9,18)],
	 (9,18): [(8,18),(9,17),(10,18),(9,19)],
	 (9,19): [(8,19),(9,18),(10,19)],

         (10,0): [(9,0),       (11,0),(10,1)],
       	 (10,1): [(9,1),(10,0),(11,1),(10,2)],
	 (10,2): [(9,2),(10,1),(11,2),(10,3)],
	 (10,3): [(9,3),(10,2),(11,3),(10,4)],
	 (10,4): [(9,4),(10,3),(11,4),(10,5)],
	 (10,5): [(9,5),(10,4),(11,5),(10,6)],
	 (10,6): [(9,6),(10,5),(11,6),(10,7)],
	 (10,7): [(9,7),(10,6),(11,7),(10,8)],
	 (10,8): [(9,8),(10,7),(11,8),(10,9)],
	 (10,9): [(9,9),(10,8),(11,9),(10,10)],
	 (10,10): [(9,10),(10,9),(11,10),(10,11)],
	 (10,11): [(9,11),(10,10),(11,11),(10,12)],
	 (10,12): [(9,12),(10,11),(11,12),(10,13)],
	 (10,13): [(9,13),(10,12),(11,13),(10,14)],
	 (10,14): [(9,14),(10,13),(11,14),(10,15)],
	 (10,15): [(9,15),(10,14),(11,15),(10,16)],
	 (10,16): [(9,16),(10,15),(11,16),(10,17)],
	 (10,17): [(9,17),(10,16),(11,17),(10,18)],
	 (10,18): [(9,18),(10,17),(11,18),(10,19)],
	 (10,19): [(9,19),(10,18),(11,19)],
         
         (11,0): [(10,0),       (12,0),(11,1)],
       	 (11,1): [(10,1),(11,0),(12,1),(11,2)],
	 (11,2): [(10,2),(11,1),(12,2),(11,3)],
	 (11,3): [(10,3),(11,2),(12,3),(11,4)],
	 (11,4): [(10,4),(11,3),(12,4),(11,5)],
	 (11,5): [(10,5),(11,4),(12,5),(11,6)],
	 (11,6): [(10,6),(11,5),(12,6),(11,7)],
	 (11,7): [(10,7),(11,6),(12,7),(11,8)],
	 (11,8): [(10,8),(11,7),(12,8),(11,9)],
	 (11,9): [(10,9),(11,8),(12,9),(11,10)],
	 (11,10): [(10,10),(11,9),(12,10),(11,11)],
	 (11,11): [(10,11),(11,10),(12,11),(11,12)],
	 (11,12): [(10,12),(11,11),(12,12),(11,13)],
	 (11,13): [(10,13),(11,12),(12,13),(11,14)],
	 (11,14): [(10,14),(11,13),(12,14),(11,15)],
	 (11,15): [(10,15),(11,14),(12,15),(11,16)],
	 (11,16): [(10,16),(11,15),(12,16),(11,17)],
	 (11,17): [(10,17),(11,16),(12,17),(11,18)],
	 (11,18): [(10,18),(11,17),(12,18),(11,19)],
	 (11,19): [(10,19),(11,18),(12,19)],

         (12,0): [(11,0),       (13,0),(12,1)],
       	 (12,1): [(11,1),(12,0),(13,1),(12,2)],
	 (12,2): [(11,2),(12,1),(13,2),(12,3)],
	 (12,3): [(11,3),(12,2),(13,3),(12,4)],
	 (12,4): [(11,4),(12,3),(13,4),(12,5)],
	 (12,5): [(11,5),(12,4),(13,5),(12,6)],
	 (12,6): [(11,6),(12,5),(13,6),(12,7)],
	 (12,7): [(11,7),(12,6),(13,7),(12,8)],
	 (12,8): [(11,8),(12,7),(13,8),(12,9)],
	 (12,9): [(11,9),(12,8),(13,9),(12,10)],
	 (12,10): [(11,10),(12,9),(13,10),(12,11)],
	 (12,11): [(11,11),(12,10),(13,11),(12,12)],
	 (12,12): [(11,12),(12,11),(13,12),(12,13)],
	 (12,13): [(11,13),(12,12),(13,13),(12,14)],
	 (12,14): [(11,14),(12,13),(13,14),(12,15)],
	 (12,15): [(11,15),(12,14),(13,15),(12,16)],
	 (12,16): [(11,16),(12,15),(13,16),(12,17)],
	 (12,17): [(11,17),(12,16),(13,17),(12,18)],
	 (12,18): [(11,18),(12,17),(13,18),(12,19)],
	 (12,19): [(11,19),(12,18),(13,19)],

	 (13,0): [(12,0),       (14,0),(13,1)],
       	 (13,1): [(12,1),(13,0),(14,1),(13,2)],
	 (13,2): [(12,2),(13,1),(14,2),(13,3)],
	 (13,3): [(12,3),(13,2),(14,3),(13,4)],
	 (13,4): [(12,4),(13,3),(14,4),(13,5)],
	 (13,5): [(12,5),(13,4),(14,5),(13,6)],
	 (13,6): [(12,6),(13,5),(14,6),(13,7)],
	 (13,7): [(12,7),(13,6),(14,7),(13,8)],
	 (13,8): [(12,8),(13,7),(14,8),(13,9)],
	 (13,9): [(12,9),(13,8),(14,9),(13,10)],
	 (13,10): [(12,10),(13,9),(14,10),(13,11)],
	 (13,11): [(12,11),(13,10),(14,11),(13,12)],
	 (13,12): [(12,12),(13,11),(14,12),(13,13)],
	 (13,13): [(12,13),(13,12),(14,13),(13,14)],
	 (13,14): [(12,14),(13,13),(14,14),(13,15)],
	 (13,15): [(12,15),(13,14),(14,15),(13,16)],
	 (13,16): [(12,16),(13,15),(14,16),(13,17)],
	 (13,17): [(12,17),(13,16),(14,17),(13,18)],
	 (13,18): [(12,18),(13,17),(14,18),(13,19)],
	 (13,19): [(12,19),(13,18),(14,19)],

         (14,0): [(13,0),       (15,0),(14,1)],
       	 (14,1): [(13,1),(14,0),(15,1),(14,2)],
	 (14,2): [(13,2),(14,1),(15,2),(14,3)],
	 (14,3): [(13,3),(14,2),(15,3),(14,4)],
	 (14,4): [(13,4),(14,3),(15,4),(14,5)],
	 (14,5): [(13,5),(14,4),(15,5),(14,6)],
	 (14,6): [(13,6),(14,5),(15,6),(14,7)],
	 (14,7): [(13,7),(14,6),(15,7),(14,8)],
	 (14,8): [(13,8),(14,7),(15,8),(14,9)],
	 (14,9): [(13,9),(14,8),(15,9),(14,10)],
	 (14,10): [(13,10),(14,9),(15,10),(14,11)],
	 (14,11): [(13,11),(14,10),(15,11),(14,12)],
	 (14,12): [(13,12),(14,11),(15,12),(14,13)],
	 (14,13): [(13,13),(14,12),(15,13),(14,14)],
	 (14,14): [(13,14),(14,13),(15,14),(14,15)],
	 (14,15): [(13,15),(14,14),(15,15),(14,16)],
	 (14,16): [(13,16),(14,15),(15,16),(14,17)],
	 (14,17): [(13,17),(14,16),(15,17),(14,18)],
	 (14,18): [(13,18),(14,17),(15,18),(14,19)],
	 (14,19): [(13,19),(14,18),(15,19)],

         (15,0): [(14,0),       (16,0),(15,1)],
       	 (15,1): [(14,1),(15,0),(16,1),(15,2)],
	 (15,2): [(14,2),(15,1),(16,2),(15,3)],
	 (15,3): [(14,3),(15,2),(16,3),(15,4)],
	 (15,4): [(14,4),(15,3),(16,4),(15,5)],
	 (15,5): [(14,5),(15,4),(16,5),(15,6)],
	 (15,6): [(14,6),(15,5),(16,6),(15,7)],
	 (15,7): [(14,7),(15,6),(16,7),(15,8)],
	 (15,8): [(14,8),(15,7),(16,8),(15,9)],
	 (15,9): [(14,9),(15,8),(16,9),(15,10)],
	 (15,10): [(14,10),(15,9),(16,10),(15,11)],
	 (15,11): [(14,11),(15,10),(16,11),(15,12)],
	 (15,12): [(14,12),(15,11),(16,12),(15,13)],
	 (15,13): [(14,13),(15,12),(16,13),(15,14)],
	 (15,14): [(14,14),(15,13),(16,14),(15,15)],
	 (15,15): [(14,15),(15,14),(16,15),(15,16)],
	 (15,16): [(14,16),(15,15),(16,16),(15,17)],
	 (15,17): [(14,17),(15,16),(16,17),(15,18)],
	 (15,18): [(14,18),(15,17),(16,18),(15,19)],
	 (15,19): [(14,19),(15,18),(16,19)],

         (16,0): [(15,0),       (17,0),(16,1)],
       	 (16,1): [(15,1),(16,0),(17,1),(16,2)],
	 (16,2): [(15,2),(16,1),(17,2),(16,3)],
	 (16,3): [(15,3),(16,2),(17,3),(16,4)],
	 (16,4): [(15,4),(16,3),(17,4),(16,5)],
	 (16,5): [(15,5),(16,4),(17,5),(16,6)],
	 (16,6): [(15,6),(16,5),(17,6),(16,7)],
	 (16,7): [(15,7),(16,6),(17,7),(16,8)],
	 (16,8): [(15,8),(16,7),(17,8),(16,9)],
	 (16,9): [(15,9),(16,8),(17,9),(16,10)],
	 (16,10): [(15,10),(16,9),(17,10),(16,11)],
	 (16,11): [(15,11),(16,10),(17,11),(16,12)],
	 (16,12): [(15,12),(16,11),(17,12),(16,13)],
	 (16,13): [(15,13),(16,12),(17,13),(16,14)],
	 (16,14): [(15,14),(16,13),(17,14),(16,15)],
	 (16,15): [(15,15),(16,14),(17,15),(16,16)],
	 (16,16): [(15,16),(16,15),(17,16),(16,17)],
	 (16,17): [(15,17),(16,16),(17,17),(16,18)],
	 (16,18): [(15,18),(16,17),(17,18),(16,19)],
	 (16,19): [(15,19),(16,18),(17,19)],

         (17,0): [(16,0),              (17,1)],
       	 (17,1): [(16,1),(17,0),       (17,2)],
	 (17,2): [(16,2),(17,1),       (17,3)],
	 (17,3): [(16,3),(17,2),       (17,4)],
	 (17,4): [(16,4),(17,3),       (17,5)],
	 (17,5): [(16,5),(17,4),       (17,6)],
	 (17,6): [(16,6),(17,5),       (17,7)],
	 (17,7): [(16,7),(17,6),       (17,8)],
	 (17,8): [(16,8),(17,7),       (17,9)],
	 (17,9): [(16,9),(17,8),       (17,10)],
	 (17,10): [(16,10),(17,9),       (17,11)],
	 (17,11): [(16,11),(17,10),       (17,12)],
	 (17,12): [(16,12),(17,11),       (17,13)],
	 (17,13): [(16,13),(17,12),       (17,14)],
	 (17,14): [(16,14),(17,13),       (17,15)],
	 (17,15): [(16,15),(17,14),       (17,16)],
	 (17,16): [(16,16),(17,15),       (17,17)],
	 (17,17): [(16,17),(17,16),       (17,18)],
	 (17,18): [(16,18),(17,17),       (17,19)],
	 (17,19): [(16,19),(17,18)               ]
	}

pygame.init()

class mouse(pygame.Rect): #Clase para obtener posicion x y y del mouse
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos() 

class boton(pygame.sprite.Sprite): #Clase en la que se definen los botones y sus posiciones
    def __init__(self,imagen1, imagen2, imagen3, x, y):
        self.boton_normal = imagen1
        self.boton_claro = imagen2
        self.boton_oscuro = imagen3
        self.boton_actual = self.boton_normal
        self.rect = self.boton_actual.get_rect() #Se crea un rectángulo en el boton para colicionar con el mouse
        self.rect.left, self.rect.top = (x,y)

    def update(self,display_game,mouse, x, y): #Pega la imagen del boton en la pantalla
        if mouse.colliderect(self.rect): # Condición si pasa el mouse encima del boton, este se ilumina(carga otra imagen)
            self.boton_actual = self.boton_claro 
        else:
            self.boton_actual = self.boton_normal
        display_game.blit(self.boton_actual,(x,y))
    def update2(self,display_game, mouse, name, x, y): #Permite que el boton de start se active o no
        if name != "": #Condición que permite que el boton de start se active y se ponga normal
            if mouse.colliderect(self.rect): # Condición si pasa el mouse encima del boton, este se ilumina(carga otra imagen)
                self.boton_actual = self.boton_claro
            else:
                self.boton_actual = self.boton_normal
        else:
            self.boton_actual = self.boton_oscuro
        display_game.blit(self.boton_actual,(x,y))



class snake(): #Clase en la que se definen los confites
    def __init__(self, imgU,imgD,imgL,imgR):
        self.snakeImgR =  imgR
        self.snakeImgL =  imgL
        self.snakeImgU =  imgU
        self.snakeImgD =  imgD
        self.imgActual = self.snakeImgL
        self.posicionActual = 'L'
        
    def update(self, display_game, x, y,img_f): #Pega la snake
        display_game.blit(img_f,(0,0))
        display_game.blit(self.imgActual,(x,y))
        #pygame.display.update()
        
    def cambiaTipo(self,direccion):
        if direccion == 'U':
            self.imgActual = self.snakeImgU
            self.posicionActual = 'U'
        if direccion == 'D':
            self.imgActual = self.snakeImgD
            self.posicionActual = 'D'
        if direccion == 'L':
            self.imgActual = self.snakeImgL
            self.posicionActual = 'L'
        if direccion == 'R':
            self.imgActual = self.snakeImgR
            self.posicionActual = 'R'
        
    def ataque(self,display_game, x, y,img_f,enemy,posH):
        x=x*30
        y=y*30
        
        a=x
        b=y
        for n in range(37):
            img_atq = pygame.image.load("ataque"+str(self.posicionActual)+"/frame_"+str(n)+"_delay-0.1s.png")
            display_game.blit(img_atq,(a,b))
            pygame.display.update()
            time.sleep(0.039)
            display_game.blit(img_f,(0,0))
            enemy.carga(display_game)
        #self.update(display_game,x,y,img_f)
        enemy.elimina(posH)
        enemy.carga(display_game)
        

class hollow():
    def __init__(self, imgR, lista):
        self.hollowImgR =  imgR
        self.listaH = []
        for n in lista:
            self.listaH.append(n)
        
    def carga(self, display_game): #Pega la snake
        print(self.listaH)
        for n in self.listaH:
            display_game.blit(self.hollowImgR,(n[1]*30,n[0]*30))
            refresca_puntaje(display_game)
        pygame.display.update()
    def elimina(self, pos):
        self.listaH.remove(pos)


def busquedaProfundidad(grafo,matriz,objetivo, inicio):
    visitados = []
    
    pila = []
    origen = inicio
    #SE COLOCA EL VÉRTICE ORIGEN EN UNA PILA
    pila.append(origen)
    while pila:
            #DESAPILAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
            actual = pila.pop(0)
            #SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
            if actual not in visitados:
                #PROCESAR (IMPRIMIR) EL VÉRTICE ACTUAL
                    #COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
                visitados.append(actual)
            #PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO,
            #        Y QUE NO HA SIDO VISITADO:
            #        APILAR EL VERTICE
                if matriz[actual[0]][actual[1]] == objetivo:
                    #print(actual)
                    return actual
                else:
                    for key in grafo[actual]:
                            if key not in visitados:
                                    pila.append(key)
def imprimeMatriz(matriz):
    os.system('cls')
    for i in range (18):
        print(matriz[i])

    print("------------------------------------------------------------------------------------------")

    time.sleep(0.5)

def refresca_puntaje(display_game):
        fuente = pygame.font.Font(None, 45)

        global cont
        text = str(cont)
        mensaje = fuente.render(text, 1, (255, 255, 255))
        display_game.blit(mensaje, (670,60))

        text = "Movimientos"
        mensaje = fuente.render(text, 1, (255, 255, 255))
        display_game.blit(mensaje, (605,90))

        segundos = pygame.time.get_ticks()//1000
        
        
        text = str(segundos)
        mensaje = fuente.render(text, 1, (255, 255, 255))
        display_game.blit(mensaje, (675,130))

        text = "Tiempo"
        mensaje = fuente.render(text, 1, (255, 255, 255))
        display_game.blit(mensaje, (627,160))
    
def moverSnake(matriz,posSnake,posObjetivo,snake,display_game,img_f,enemy):
    global cont
    cont+=1
    pygame.display.update()
    time.sleep(0.050)
    if posSnake == posObjetivo:
        snake.ataque(display_game,posSnake[1],posSnake[0],img_f,enemy,posSnake)
        
        return matriz
    else:
        if posSnake[0]!= posObjetivo[0]:
            if posSnake[0]>posObjetivo[0]:
                posSnakeAux = (posSnake[0]-1,posSnake[1])
                matriz[posSnakeAux[0]][posSnakeAux[1]] = matriz[posSnake[0]][posSnake[1]]
                matriz[posSnake[0]][posSnake[1]] = '0'
                snake.cambiaTipo('U')
                snake.update(display_game,(posSnakeAux[1]*30),(posSnakeAux[0]*30),img_f)
                enemy.carga(display_game)
                pygame.display.update()
                moverSnake(matriz,posSnakeAux,posObjetivo,snake,display_game,img_f,enemy)
                return matriz
            else:
                posSnakeAux = (posSnake[0]+1,posSnake[1])
                matriz[posSnakeAux[0]][posSnakeAux[1]] = matriz[posSnake[0]][posSnake[1]]
                matriz[posSnake[0]][posSnake[1]] = '0'
                snake.cambiaTipo('D')
                snake.update(display_game,(posSnakeAux[1]*30),(posSnakeAux[0]*30),img_f)
                enemy.carga(display_game)
                pygame.display.update()
                moverSnake(matriz,posSnakeAux,posObjetivo,snake,display_game,img_f,enemy)
                return matriz

        elif posSnake[1]!=posObjetivo[1]:
            if posSnake[1]>posObjetivo[1]:
                posSnakeAux = (posSnake[0],posSnake[1]-1)
                matriz[posSnakeAux[0]][posSnakeAux[1]] = matriz[posSnake[0]][posSnake[1]]
                matriz[posSnake[0]][posSnake[1]] = '0'
                snake.cambiaTipo('R')
                snake.update(display_game,posSnakeAux[1]*30,posSnakeAux[0]*30,img_f)
                enemy.carga(display_game)
                pygame.display.update()
                moverSnake(matriz,posSnakeAux,posObjetivo,snake,display_game,img_f,enemy)
                return matriz
            else:
                posSnakeAux = (posSnake[0],posSnake[1]+1)
                matriz[posSnakeAux[0]][posSnakeAux[1]] = matriz[posSnake[0]][posSnake[1]]
                matriz[posSnake[0]][posSnake[1]] = '0'
                snake.cambiaTipo('L')
                snake.update(display_game,posSnakeAux[1]*30,posSnakeAux[0]*30,img_f)
                enemy.carga(display_game)
                pygame.display.update()
                moverSnake(matriz,posSnakeAux,posObjetivo,snake,display_game,img_f,enemy)
                return matriz

        else:
            return matriz
def main():
    matriz = []

    for i in range (18):
        matriz.append(['0']*20)
    

    
    matriz[0][0] = '1'
    matriz[9][5] = '*'
    matriz[2][11] = '*'
    matriz[8][18] = '*'
    matriz[17][14] = '*'
    matriz[13][19] = '*'
    listaHollow = [(9,5),(2,11),(8,18),(17,14),(13,19)]
     
    '''"posiciones (10,6) - (3,12) – (9,19) – (18,5) – (14,20) y la"'''
    menu(matriz,listaHollow)
    '''while True:
        #time.sleep(10)
        #imprimeMatriz(matriz)
        #time.sleep(10)
        posSnake = busquedaProfundidad(grafo,matriz,'1',(5,5))
        print(posSnake)
        #time.sleep(10)
        posObjetivo = busquedaProfundidad(grafo,matriz,'*',posSnake)

        if posObjetivo != None:
            matriz = moverSnake(matriz,posSnake,posObjetivo,cont)
            #busquedaProfunda(grafo,matriz)
        else:
            break'''



def juego(name, matriz,listaHollow): #Función juego, se encuentra todo el juego, despues del menú
    pygame.init() #Inicializa pygame

    display_width = 800 #Largo de la pantalla
    display_height = 600 #Ancho de la pantalla
    display_game = pygame.display.set_mode((display_width,display_height)) #Establece la ventana del juego con 800x600

    reloj2 = pygame.time.Clock() #Establece el reloj

    mouse2 = mouse()# Establece el mouse

    pygame.mixer.music.load("bleach ost 1 battle ignition 18.mp3") #Carga la canción que será ejecutada durante el juego
    pygame.mixer.music.play(5) #Establece la cantidad de veces que la canción será repetida

    imagen_f = pygame.image.load("bleach_py2.jpg") #Carga la imagen de fondo
    display_game.blit(imagen_f,(0,0)) #Pega la imagen de fondo

    imgU = pygame.image.load("ataqueU/frame_0_delay-0.1s.png") #Imagen
    imgD = pygame.image.load("ataqueD/frame_0_delay-0.1s.png") #Imagen
    imgL = pygame.image.load("ataqueL/frame_0_delay-0.1s.png") #Imagen
    imgR = pygame.image.load("ataqueR/frame_0_delay-0.1s.png") #Imagen

    PJ = snake(imgU,imgD,imgL,imgR)

    imgH = pygame.image.load("full3.png")
    Enemy = hollow(imgH,listaHollow)
    Enemy.carga(display_game)
            
    fail = False
    while not fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        posSnake = busquedaProfundidad(grafo,matriz,'1',(5,5))
        print(posSnake)
        #time.sleep(10)
        posObjetivo = busquedaProfundidad(grafo,matriz,'*',posSnake)
        Enemy.carga(display_game)

        if posObjetivo != None:
            matriz = moverSnake(matriz,posSnake,posObjetivo,PJ,display_game,imagen_f,Enemy)
        else:
            fail = True
        
        mouse2.update()
        reloj2.tick(60)
        pygame.display.update()

    
def menu(matriz,listaHollow):
    pygame.init()
    
    pygame.mixer.music.load("Bleach.D-tecnoLife.mp3")
    pygame.mixer.music.play(5)

    display_width = 800
    display_height = 600

    display_game = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Bleach Souls Sagas")

    reloj1 = pygame.time.Clock()
    mouse1 = mouse()
        
    img_ng = pygame.image.load("new_game.png")
    img_ng2 = pygame.image.load("new_game2.png")
    boton_ng = boton(img_ng, img_ng2, img_ng, 315, 485)

    img_opt = pygame.image.load("options.png")
    img_opt2 = pygame.image.load("options2.png")
    boton_opt = boton(img_opt, img_opt2, img_opt, 620, 545)

    img_ex = pygame.image.load("exit.png")
    img_ex2 = pygame.image.load("exit2.png")
    boton_ex = boton(img_ex, img_ex2, img_ex, 315, 545)

    img_eyn = pygame.image.load("enter_your_name.png")
    boton_eyn = boton(img_eyn, img_eyn, img_eyn, 300, 100)

    img_st = pygame.image.load("start.png")
    img_st2 = pygame.image.load("start2.png")
    img_st3 = pygame.image.load("start3.png")
    boton_st = boton(img_st, img_st2, img_st3, 315, 485)
    name = ""
    b_cambio = 0

    img_b = pygame.image.load("back.png")
    img_b2 = pygame.image.load("back2.png")
    boton_b = boton(img_b, img_b2, img_b, 315, 545)  
        
    imagen_f = pygame.image.load("bleach_py.jpg")
    display_game.blit(imagen_f,(0,0))

     
    
    
    fuente = pygame.font.Font(None, 47)

    


    fail = False
    botones_menu1 = True
    eventos_menu1 = True
    botones_menu2 = False
    eventos_menu2 = False
    evento_escritura = False
    while not fail:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if eventos_menu1 == True:
                    if mouse1.colliderect(boton_ex.rect):
                        pygame.quit()
                        quit()
                    if mouse1.colliderect(boton_ng.rect):
                        botones_menu1 = False
                        eventos_menu1 = False
                        botones_menu2 = True
                        eventos_menu2 = True
                        evento_escritura = True
                if eventos_menu2 == True:
                    if mouse1.colliderect(boton_b.rect):
                        botones_menu1 = True
                        eventos_menu1 = True
                        botones_menu2 = False
                        eventos_menu2 = False
                        evento_escritura = False
                        name = ""
                        display_game.blit(imagen_f,(0,0))
                        b_cambio = 0
                    if mouse1.colliderect(boton_st.rect):
                        if b_cambio == 1:
                            botones_menu2 = False
                            eventos_menu2 = False
                            evento_escritura = False
                            pygame.mixer.quit()
                            imagen_f = pygame.image.load("cambio.jpeg")
                            display_game.blit(imagen_f,(0,0))
                            pygame.display.update()
                            pygame.time.wait(3000)
                            juego(name, matriz,listaHollow)
            if event.type == pygame.KEYDOWN:
                if evento_escritura == True:
                    if event.unicode.isalpha():
                        if len(name) < 8:
                            name += event.unicode
                    if event.key == K_BACKSPACE:
                        name = name[:-1]
                    if event.key == K_RETURN:
                        if b_cambio == 1:
                            botones_menu2 = False
                            eventos_menu2 = False
                            evento_escritura = False
                            pygame.mixer.quit()
                            imagen_f = pygame.image.load("cambio.jpeg")
                            display_game.blit(imagen_f,(0,0))
                            pygame.display.update()
                            pygame.time.wait(3000)
                            juego(name, matriz,listaHollow)
                    if event.key == K_ESCAPE:
                        name = ""
                    if name == "":
                        b_cambio = 0
                    else:
                        b_cambio = 1
                print(name)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mensaje = fuente.render(name, True, (255, 255, 255))
        a = mensaje.get_rect()
        a.center = display_game.get_rect().center 
        display_game.blit(mensaje, a)
        display_game.blit(imagen_f,(0,0))
        display_game.blit(mensaje, a)
        
        if botones_menu1 == True:
            boton_ng.update(display_game, mouse1, 315, 485)
            boton_ex.update(display_game, mouse1, 315, 545)
            boton_opt.update(display_game, mouse1, 620, 545)
        if botones_menu2 == True:
            boton_b.update(display_game, mouse1, 315, 545)
            boton_st.update2(display_game, mouse1, name, 315, 485)
            boton_eyn.update(display_game, mouse1, 300, 100)


        reloj1.tick(60)
        mouse1.update()
        pygame.display.update()



main()

