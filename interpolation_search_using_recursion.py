def interpolation_search_using_recursion(arr,element,low,high):
    interpolation = low + (((high-low)*(element-arr[low]))//(arr[high]-arr[low]))
    if interpolation <= high and interpolation >= low:
        if element == arr[interpolation]:
            return f'ELEMENT FOUND AT INDEX {interpolation}'
        elif element < arr[interpolation]:
            return interpolation_search_using_recursion(arr,element,low,interpolation-1)
        elif element > arr[interpolation]:
            return interpolation_search_using_recursion(arr,element,interpolation+1,high)

    return 'ELEMENT NOT FOUND!'

arr = [-213,10,43,49,54,100,345,546,765,1000,5400]
print(interpolation_search_using_recursion(arr,101,0,len(arr)-1))