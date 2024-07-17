
# Foodly

Welcome to the Streamlit app that utilizes the [Open Food Facts Python SDK](https://github.com/openfoodfacts/openfoodfacts-python) to fetch and display food product data from [https://de.openfoodfacts.org/](https://de.openfoodfacts.org/). This project was created for a mini hackathon organized by Kevin Chromik.

## Demo

https://vimeo.com/985836404?share=copy

## Contributors

- [mirixy](https://github.com/mirixy)
- [cipher-shad0w](https://github.com/cipher-shad0w)
- [arvedb](https://github.com/arvedb)

## Features

- User-friendly interface to search for food products.
- Search for food products by text.
- Fetches nutriscore and nutriments data.
- Displays results in a structured and easy-to-read format.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   cd frontend
   streamlit run app.py
   ```

3. **Enter the name of a food product in the text input field and submit to get a list of found products details. Click the desired product to get nutriscore and nutriments data.**

## Project Structure

- `test.py`: Main file to run the Streamlit app.
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- [Streamlit](https://streamlit.io/): Framework for creating interactive web applications.
- [Open Food Facts Python SDK](https://github.com/openfoodfacts/openfoodfacts-python): Python library for interacting with the Open Food Facts database.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

Special thanks to Kevin Chromik for organizing the mini hackathon.

---

If you have any questions or need further assistance, please feel free to contact any of the contributors.

Happy coding!
