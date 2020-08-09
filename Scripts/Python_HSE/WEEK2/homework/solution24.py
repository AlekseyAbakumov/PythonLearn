l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())

answer = 0

if hc // (h1 + h2):
    L1 = l1 if l1 >= l2 else l2
    W1 = w1 if w1 >= w2 else w2
    L2, W2 = W1, L1
    if (lc // L1 and wc // W1) or (lc // L2 and wc // W2):
        answer = 1

    L1 = l1 if l1 >= w2 else w2
    W1 = w1 if w1 >= l2 else l2
    L2, W2 = W1, L1
    if (lc // L1 and wc // W1) or (lc // L2 and wc // W2):
        answer = 1

if hc // h1 and hc // h2:
    if not answer:
        L1 = l1 if l1 >= l2 else l2
        W1 = w1 + w2
        L2, W2 = W1, L1
        if (lc // L1 and wc // W1) or (lc // L2 and wc // W2):
            answer = 1

    if not answer:
        L1 = l1 + l2
        W1 = w1 if w1 >= w2 else w2
        L2, W2 = W1, L1
        if (lc // L1 and wc // W1) or (lc // L2 and wc // W2):
            answer = 1

    if not answer:
        L1 = l1 if l1 >= w2 else w2
        W1 = w1 + l2
        L2, W2 = W1, L1
        if (lc // L1 and wc // W1) or (lc // L2 and wc // W2):
            answer = 1

    if not answer:
        L1 = l1 + w2
        W1 = w1 if w1 >= l2 else l2
        L2, W2 = W1, L1
        if (lc // L1 and wc // W1) or (lc // L2 and wc // W2):
            answer = 1

if answer:
    print('YES')
else:
    print('NO')
