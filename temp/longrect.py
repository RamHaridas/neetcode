from stack import Stack

def largestRectangle(items):
    max_area = 0
    stack = Stack()
    # ITERATING THROUGH LIST
    for i in range(len(items)):
        if stack.is_empty():
            # PUSHING HEIGHT AND INDEX IF STACK IS EMPTY
            stack.push((items[i], i))
        else:
            last_item = None
            # POPPING ITEMS IF SHORT RIGHT TOWER DETECTED
            while not stack.is_empty() and stack.peek()[0] > items[i]:
                # CALCULATING AREA OF CURRENT TOWER HEIGHT MULTIPLIED BY DISTANCE BETWEEN TOWER AT TOP OF STACK
                top = stack.pop()
                width = i - top[1]
                area = width * items[i]
                max_area = max(area, max_area)
                # SAVING LAST TOWER WITH POSITION OF TOWER AT TOP
                last_item = (items[i],top[1])
            else:
                # PUSHING IF TOWER AT RIGHT IS TALLER THAN TOWER AT TOP
                stack.push((items[i], i))
            if last_item:
                # PUSHING LAST ITEM WITH UPDATED INDEX
                stack.push(last_item)
    
    # POPPING STACK UNTIL IT IS EMPTY TO CALCULATE AREA OF RESIDUAL TOWERS
    while not stack.is_empty():
        # SUBTRACTING THE POSITION OF TOWER FROM LENGTH TO DETERMINE WIDTH
        top = stack.pop()
        width = len(items) - top[1]
        area = top[0] * width
        max_area = max(max_area, area)

    # RETURNING MAX AREA
    return max_area

res = largestRectangle([2,1,2])
print(res)