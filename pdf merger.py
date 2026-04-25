import PyPDF2

def merge_pdfs(pdf_list, output):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()
    print(f"Merged into {output}")

# Example usage
merge_pdfs(["file1.pdf", "file2.pdf"], "combined.pdf")
