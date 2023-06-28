# auto-enterprise

Automating Wi-Fi Enterprise tests on Linux is dead-easy, everything can be configured from the command line. MacOS takes a different approach.

## Features

- Automate MacOS Enterprise Wi-Fi connections
- Command-line interface for ease of use and scripting

## Requirements

- MacOS
- Python

## Getting Started

1. Clone the repository:
    ```
    git clone https://github.com/nullsurface/auto-enterprise.git
    ```

2. Navigate to the cloned repository:
    ```
    cd auto-enterprise
    ```

3. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

4. Two ways to use auto-enterprise.
    * Run the script to connect you Mac to Enterprise Wi-Fi:
    ```
    python connect.py
    ```
    * Import the module in python
    ```
    import MacAutoEnt
    ```
## Documentation

As this is a small framework, most of the usage information can be found in the script's code comments. Please read through the comments in `MacAutoEnterprise.py` for detailed information on usage and customization.

## Contributions

Contributions to `auto-enterprise` are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the Apache-2.0 license.

## Support

For any issues or feature requests, please open an issue on the GitHub repository.

## Community

If you find this project useful, please consider giving it a star on GitHub.
