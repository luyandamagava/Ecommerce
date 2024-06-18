# Ecommerce

**Project Title:** Ecommerce

**Description:**

This project is an ecommerce website that allows users to create, add, and delete new listings. Users can add listings that others can bid on, providing a dynamic and interactive online marketplace.

## Key Features

- **Create Listings:** Implemented forms for comprehensive listing creation, including title, description, starting bid, optional image, and category.
- **View Active Listings:** Designed a dynamic listings page showcasing key details and images.
- **Detailed Listing Views:** Created informative listing pages with bidding functionality, current price tracking, and a 'close auction' feature for listing owners.
- **Watchlists:** Enabled users to curate personalized watchlists and easily navigate to their favorite listings.
- **Comments:** Added commenting functionality to listing pages for user discussions.
- **Category Filtering:** Implemented category-based browsing for efficient item discovery.
- **User Authentication and Authorization:** Integrated user management, ensuring actions were restricted to authenticated users.

## Technologies Used

- **Backend:** Django (Python), MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Django REST Framework:** For robust back-end API development
- **MySQL:** For reliable and scalable database management

## Getting Started

### Prerequisites:

- Python 3.x
- Django
- MySQL (or your preferred database)
- Node.js (to install required packages)

### Installation:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/luyandamagava/Ecommerce
   ```
2. **Navigate into the project directory:**
   ```bash
   cd Ecommerce
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```
4. **Activate the virtual environment:**
   - **Linux/macOS:**
     ```bash
     source env/bin/activate
     ```
   - **Windows:**
     ```bash
     env\Scripts\activate
     ```
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Set up your database:** (instructions may vary depending on your database setup)
7. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
8. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
9. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
10. **Access the project:** Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Usage

1. **Create a new account** using the signup form.
2. **Log in** to access the main listings page.
3. **Create new listings** with detailed descriptions, starting bids, and images.
4. **Bid on listings** and track current prices in real-time.
5. **Add listings** to your personalized watchlist for easy access.
6. **Comment on listings** to engage in discussions with other users.
7. **Filter listings by category** to find items of interest quickly.

## Contributing

We welcome contributions to this project! Here's how:

1. **Fork the repository.**
2. **Create a new branch** for your feature:
   ```bash
   git checkout -b my-awesome-feature
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push your branch** to your fork:
   ```bash
   git push origin my-awesome-feature
   ```
5. **Create a new pull request.**

## Future Development

- **Enhanced Search:** Implement search functionality for listings, users, and categories.
- **Direct Messaging:** Allow users to send private messages.
- **Advanced Filtering:** Add more advanced filtering options for listings.

## Contact

If you have questions, suggestions, or bug reports, please feel free to open an issue on the repository or contact me at [luyandamagava@gmail.com](mailto:luyandamagava@gmail.com).

## Show Your Support

If you find this project useful, please consider starring the repository!

