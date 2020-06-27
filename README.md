1. Installing dependencies:

    After creating a new virtual environment, make sure that you have Pyton 3.6. Then run
    `pip install -r requirements.txt` to get dependencies. Note that some packages need to 
    have C++ libraries to be built.

2. Running the application:

    The application should run with sudo privilages. Exapmle run for `sudo python3 run.py`. After
    running this, there will be a window opened, adn for outgoing packages promts should be appeared.

    Note: After you run the application all outgoing network will be blocked except DNS calls. You need to allow or deny applications one by one in order to have a custom configured network.

    Note: We recommend that close voice call applications or other UDP applications before starting the app, then start your voice calls in order to have good experience.