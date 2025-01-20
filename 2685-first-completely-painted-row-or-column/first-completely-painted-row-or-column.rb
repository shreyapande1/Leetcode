def first_complete_index(arr, mat)
    m, n = mat.length, mat[0].length
    
    # Create hash map to store positions of numbers in matrix
    pos = {}
    (0...m).each do |i|
        (0...n).each do |j|
            pos[mat[i][j]] = [i, j]
        end
    end
    
    # Arrays to track painted cells in each row and column
    row_count = Array.new(m, 0)
    col_count = Array.new(n, 0)
    
    # Process array elements
    arr.each_with_index do |num, idx|
        row, col = pos[num]
        row_count[row] += 1
        col_count[col] += 1
        
        # Check if any row or column is complete
        return idx if row_count[row] == n || col_count[col] == m
    end
    
    -1  # Should never reach here given constraints
end