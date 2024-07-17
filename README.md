
# Foodly

Welcome to the Streamlit app that utilizes the [Open Food Facts Python SDK](https://github.com/openfoodfacts/openfoodfacts-python) to fetch and display food product data from [https://de.openfoodfacts.org/](https://de.openfoodfacts.org/). This project was created for a mini hackathon organized by Kevin Chromik.

## Demo

(https://vimeo.com/985836404?share=copy)
<iframe src="https://player.vimeo.com/video/985836404?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Foodly Demo"></iframe>


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
   streamlit run test.py
   ```

3. **Enter the name of a food product in the text input field and submit to get a list of found products details. Click the desired product to get nutriscore and nutriments data.**

## Project Structure

- `test.py`: Main file to run the Streamlit app.
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- [Streamlit](https://streamlit.io/): Framework for creating interactive web applications.
- [Open Food Facts Python SDK](https://github.com/openfoodfacts/openfoodfacts-python): Python library for interacting with the Open Food Facts database.

## Contributing

We welcome contributions to enhance this project. If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

Special thanks to Kevin Chromik for organizing the mini hackathon.

---

If you have any questions or need further assistance, please feel free to contact any of the contributors.

Happy coding!
