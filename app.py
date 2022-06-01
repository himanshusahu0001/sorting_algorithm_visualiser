import math
from msilib.schema import Font
from tkinter import TOP
import black
import pygame
import random
pygame.init()

# COLORS VALUE's TUPLES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BG_COLOR = WHITE

GRADIENTS = [(128, 128, 128), (160, 160, 160),
             (192, 192, 192)]  # shades of grey

FONT = pygame.font.SysFont('comicsans', 30)
LARGE_FONT = pygame.font.SysFont('comicsans', 40)


# ########################
width = 1200
height = 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algorithm visualiser")
SIDE_PAD = 100
TOP_PAD = 150
initial_x = SIDE_PAD // 2


# other functions
def generate_random_List(n, min_val, max_val):
    res = list()
    for i in range(n):
        val = random.randint(1+min_val, max_val)
        res.append(val)
    return res


def draw_list(lst, color_positions, min_val, block_width, block_height):

    pygame.draw.rect(screen, BG_COLOR, (0, TOP_PAD, width, height))

    for i, val in enumerate(lst):
        x = initial_x + i * block_width
        y = height - ((val - min_val) * block_height)
        block_color = GRADIENTS[i % 3]

        if i in color_positions:
            block_color = color_positions[i]

        pygame.draw.rect(screen, block_color,
                         (x, y, block_width, val*block_height))

# //////////////////// SORTING ALGORITHMS FUNCTIONS


def bubble_sort(lst, min_val, block_width, block_height,  ascending=True):
    for i in range(len(lst)-1):
        for j in range(len(lst) - 1 - i):
            if(lst[j] > lst[j+1] and ascending) or (lst[j] < lst[j+1] and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(lst, {j: GREEN, j+1: RED},
                          min_val, block_width, block_height)
                yield True
    return lst


def insertion_sort(lst, min_val, block_width, block_height,  ascending=True):
    for i in range(len(lst)):
        j = i
        while j > 0:
            if(lst[j-1] > lst[j] and ascending) or (lst[j-1] < lst[j] and not ascending):
                lst[j], lst[j-1] = lst[j-1], lst[j]
                draw_list(lst, {j-1: GREEN, j: RED},
                          min_val, block_width, block_height)
            j = j-1
            yield True
    return lst


def merge_sort(a, min_val, block_width, block_height,  ascending=True):
    w = 1   
    n = len(a)                                         
    while (w < n):
        l=0;
        while (l < n):
            r = min(l+(w*2-1), n-1)        
            m = min(l+w-1,n-1)
            
            n1 = m - l + 1
            n2 = r - m
            L = [0] * n1
            R = [0] * n2
            for i in range(0, n1):
                L[i] = a[l + i]
            for i in range(0, n2):
                R[i] = a[m + i + 1]
        
            i, j, k = 0, 0, l
            while i < n1 and j < n2:
                if (L[i] <= R[j] and ascending) or (L[i] >= R[j] and not ascending):
                    a[k] = L[i]
                    draw_list(a, {k: GREEN},
                          min_val, block_width, block_height)
                    yield True
                    i += 1
                else:
                    a[k] = R[j]
                    draw_list(a, {k: GREEN},
                          min_val, block_width, block_height)
                    yield True
                    j += 1
                k += 1
        
            while i < n1:
                a[k] = L[i]
                draw_list(a, {k: GREEN},
                        min_val, block_width, block_height)
                yield True
                i += 1
                k += 1
        
            while j < n2:
                a[k] = R[j]
                draw_list(a, {k: GREEN},
                        min_val, block_width, block_height)
                yield True
                j += 1
                k += 1

            l += w*2
        w *= 2
    return a


def quick_sort(arr, min_val, block_width, block_height,  ascending=True):
    l=0
    h=len(arr)-1    
    size = h - l + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    while top >= 0:
 
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        i = ( l - 1 )
        x = arr[h]
        for j in range(l, h):
            if   (arr[j] <= x and ascending) or (arr[j] >= x and not ascending):
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                draw_list(arr, {j: GREEN, j+1: RED},
                          min_val, block_width, block_height)
                yield True
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        draw_list(arr, {i+1: GREEN, h: RED},
                    min_val, block_width, block_height)
        yield True
        p =  (i + 1)

        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# MAIN FUNCTION
def main():
    n, min_val, max_val = 100, 2, 90
    lst = generate_random_List(n, min_val, max_val)
    # print(lst)
    block_width = ((width-SIDE_PAD) / n)
    # block_width = math.floor((width-SIDE_PAD) / n)
    block_height = math.floor((height - TOP_PAD) / (max_val-min_val))

    # ////////////////////////////////////////////////////////////////////////
    clock = pygame.time.Clock()
    run = True
    # ///////////////////////////////////////////////////////////////////////
    Sorting = False
    ascending = True

    screen.fill(WHITE)

    controls = FONT.render(
        "R - RESET | A - Ascending | D - Descending", 1, BLACK)
    screen.blit(controls, ((width - controls.get_width())/2, 60))

    Sorting_controls = FONT.render(
        "1 - Bubble Sort | 2 - Insertion Sort | 3 - Merge Sort | 4 - Quick Sort", 1, BLACK)
    screen.blit(Sorting_controls,
                ((width - Sorting_controls.get_width())/2, 95))

    sorting_algo = bubble_sort
    sorting_algo_genrator = None
    algo_name = "Bubble Sort"

    while run:
        clock.tick(10)

        if Sorting:
            try:
                next(sorting_algo_genrator)
            except StopIteration:
                Sorting = False
        else:
            draw_list(lst, {}, min_val, block_width, block_height)
            pygame.draw.rect(screen, BG_COLOR, (0, 0, width, 65))
            chosen_options = LARGE_FONT.render(
                f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, GREEN)
            screen.blit(chosen_options,
                        ((width - chosen_options.get_width())/2, 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = generate_random_List(n, min_val, max_val)
                block_width = ((width-SIDE_PAD) / n)
                # block_width = round((width-SIDE_PAD) / n)
                block_height = math.floor(
                    (height - TOP_PAD) / (max_val-min_val))
                Sorting = False
                draw_list(lst, {}, min_val, block_width, block_height)
            if event.key == pygame.K_SPACE and Sorting == False:
                Sorting = True
                # next line will call the sorting function
                sorting_algo_genrator = sorting_algo(
                    lst, min_val, block_width, block_height, ascending)
            if event.key == pygame.K_1:
                sorting_algo = bubble_sort
                algo_name = "Bubble Sort"
            if event.key == pygame.K_2:
                sorting_algo = insertion_sort
                algo_name = "Insertion Sort"
            if event.key == pygame.K_3:
                sorting_algo = merge_sort
                algo_name = "Merge Sort"
            if event.key == pygame.K_4:
                sorting_algo = quick_sort
                algo_name = "Quick Sort"
            if event.key == pygame.K_a:
                ascending = True
            if event.key == pygame.K_d:
                ascending = False

        # draw_list(lst, {},min_val, block_width, block_height)

        pygame.display.update()


if __name__ == "__main__":
    main()
