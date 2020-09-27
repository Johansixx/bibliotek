class Book():
    

    get_all()
        returns all attributes as a list
    set_current_value()
        this updates the current_value
    
    def __init__(self, title, author, page_count, purchase_price, purchase_year):
        
        Parameters
        ----------
        title : str
            the title of the book
        author : str
            the author of the book
        page_count : int
            the number of pages in the book
        purchase_price : float
            the purchase price of the book
        purchase_year : int
            the year the book was bought
        current_value : float
            the current value(price) of the book based on age
        
        self.title = title
        self.author = author
        self.page_count = page_count
        self.purchase_price = purchase_price
        self.purchase_year = purchase_y