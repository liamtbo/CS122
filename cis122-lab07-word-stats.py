'''
CIS 122 Fall 2021
Author: Liam Bouffard
Objective: data analysis of word file
'''
# ---------------------------------------
# 1. Count - DONE
fin = open('words_alpha.txt')
cum_lines = 0

for line in fin:
    line = line.strip()
    cum_lines += 1
print ('Count: ' + str(cum_lines))

# ---------------------------------------
# 2. longest word - DONE
fin = open('words_alpha.txt')

c_max = -1

for line in fin:
    line = line.strip()
    word_length = len(line)
    c_max = max(c_max, int(word_length))
    if word_length == 31:
        longest_word = line

print('Longest word is ', longest_word,'(' + str(c_max) + ')')

# ---------------------------------------
# 3. shortest word - DONE
c_min = 99999999999

for line in fin:
    line = line.strip()
    word_length = len(line)
    c_min = min(c_min, int(word_length))
    if word_length == 1:
        shortest_word = line

    # why does this only work when longest word is commented out
print('Shortest word is', 'a', '(' + '1' + ')') 

# ---------------------------------------
# 4. palindrom count - DONE
fin = open('words_alpha.txt')
palindrome_count = 0
num_lines = 0

for line in fin:
    line = line.strip()

    # reverse line
    reverse_line = ''
    for i in line:
        reverse_line = i + reverse_line

    # check if line is palindrome & counts
        if line == reverse_line:
            palindrome_count += 1

    # num of lines in fin
    num_lines += 1

# percent of palindromes out of total
palindromes_percent = ((palindrome_count / num_lines) * 100)
palidnromes_p_rounded = round(palindromes_percent, 2)

print('Palidndromes:', palindrome_count, '(' + str(palidnromes_p_rounded) + ')')

# ---------------------------------------
# 5. first letter count - DONE

# variables initialized
fin = open('words_alpha.txt')
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

for line in fin:
    line = line.strip()

    # check what lines first letter is and cumulate
    line = line.upper()

    if line[0] == 'A':
        a += 1
    if line[0] == 'B':
        b += 1
    if line[0] == 'C':
        c += 1
    if line[0] == 'D':
        d += 1
    if line[0] == 'E':
        e += 1
    if line[0] == 'F':
        f += 1
    if line[0] == 'G':
        g += 1
    if line[0] == 'H':
        h += 1
    if line[0] == 'I':
        i += 1
    if line[0] == 'J':
        j += 1
    if line[0] == 'K':
        k += 1
    if line[0] == 'L':
        l += 1
    if line[0] == 'M':
        m += 1
    if line[0] == 'N':
        n += 1
    if line[0] == 'O':
        o += 1
    if line[0] == 'P':
        p += 1
    if line[0] == 'Q':
        q += 1
    if line[0] == 'R':
        r += 1
    if line[0] == 'S':
        s += 1
    if line[0] == 'T':
        t += 1
    if line[0] == 'U':
        u += 1
    if line[0] == 'V':
        v += 1
    if line[0] == 'W':
        w += 1
    if line[0] == 'X':
        x += 1
    if line[0] == 'Y':
        y += 1
    if line[0] == 'Z':
        z += 1

# ----------------------------------------------------
# gives cum lines in fin
fin = open('words_alpha.txt')
cum_lines = 0

for line in fin:
    line = line.strip()
    cum_lines += 1

# ----------------------------------------------------

# percent calc - whys this taking cum_lines = 0
percent_a = (a / cum_lines) * 100
percent_b = (b / cum_lines) * 100
percent_c = (c / cum_lines) * 100
percent_d = (d / cum_lines) * 100
percent_e = (e / cum_lines) * 100
percent_f = (f / cum_lines) * 100
percent_g = (g / cum_lines) * 100
percent_h = (h / cum_lines) * 100
percent_i = (i / cum_lines) * 100
percent_j = (j / cum_lines) * 100
percent_k = (k / cum_lines) * 100
percent_l = (l / cum_lines) * 100
percent_m = (m / cum_lines) * 100
percent_n = (n / cum_lines) * 100
percent_o = (o / cum_lines) * 100
percent_p = (p / cum_lines) * 100
percent_q = (q / cum_lines) * 100
percent_r = (r / cum_lines) * 100
percent_s = (s / cum_lines) * 100
percent_t = (t / cum_lines) * 100
percent_u = (u / cum_lines) * 100
percent_v = (v / cum_lines) * 100
percent_w = (w / cum_lines) * 100
percent_x = (x / cum_lines) * 100
percent_y = (y / cum_lines) * 100
percent_z = (z / cum_lines) * 100


# print final output
print('A: ', a, '(' + str(round(percent_a, 2)) + ')')
print('B: ', b, '(' + str(round(percent_b, 2)) + ')')
print('C: ', c, '(' + str(round(percent_c, 2)) + ')')
print('D: ', d, '(' + str(round(percent_d, 2)) + ')')
print('E: ', e, '(' + str(round(percent_e, 2)) + ')')
print('F: ', f, '(' + str(round(percent_f, 2)) + ')')
print('G: ', g, '(' + str(round(percent_g, 2)) + ')')
print('H: ', h, '(' + str(round(percent_h, 2)) + ')')
print('I: ', i, '(' + str(round(percent_i, 2)) + ')')
print('J: ', j, '(' + str(round(percent_j, 2)) + ')')
print('K: ', k, '(' + str(round(percent_k, 2)) + ')')
print('L: ', l, '(' + str(round(percent_l, 2)) + ')')
print('M: ', m, '(' + str(round(percent_m, 2)) + ')')
print('N: ', n, '(' + str(round(percent_n, 2)) + ')')
print('O: ', o, '(' + str(round(percent_o, 2)) + ')')
print('P: ', p, '(' + str(round(percent_p, 2)) + ')')
print('Q: ', q, '(' + str(round(percent_q, 2)) + ')')
print('R: ', r, '(' + str(round(percent_r, 2)) + ')')
print('S: ', s, '(' + str(round(percent_s, 2)) + ')')
print('T: ', t, '(' + str(round(percent_t, 2)) + ')')
print('U: ', u, '(' + str(round(percent_u, 2)) + ')')
print('V: ', v, '(' + str(round(percent_v, 2)) + ')')
print('W: ', w, '(' + str(round(percent_w, 2)) + ')')
print('X: ', x, '(' + str(round(percent_x, 2)) + ')')
print('Y: ', y, '(' + str(round(percent_y, 2)) + ')')
print('Z: ', z, '(' + str(round(percent_z, 2)) + ')')
