# Flask & MongoDB - DevOps Assignment

A small Flask application that demonstrates:

- A `/api` route returning backend data as JSON.
- A frontend HTML form.
- Inserting submitted form data into MongoDB Atlas.
- Redirecting to a success page after a successful insert.
- Displaying errors on the same page without redirecting.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and add your MongoDB Atlas connection string, then run:

```bash
python3 app.py
```

Open:

- Form: `http://127.0.0.1:5000/`
- JSON API: `http://127.0.0.1:5000/api`

## Security

The `.env` file is ignored by Git. Never commit MongoDB credentials to GitHub.

## Submission

Add genuine screenshots to the `screenshots/` folder, paste them into the documentation, add your GitHub repository link, then compress the complete folder as `Flask_and_MongoDB_Prashant.zip`.
