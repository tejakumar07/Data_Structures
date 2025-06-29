class PascalTriangle:
    def generate_row(self, row_index):
        value = 1
        row = [value]
        for i in range(1, row_index + 1):
            value *= (row_index - i + 1)
            value //= i
            row.append(value)
        return row

    def generate_triangle(self, num_rows):
        triangle = []
        for i in range(num_rows + 1):
            triangle.append(self.generate_row(i))
        print(triangle)

if __name__ == "__main__":
    pascal = PascalTriangle()
    pascal.generate_triangle(5)
