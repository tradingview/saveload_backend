FROM python

# Set the working directory
WORKDIR /app

# copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Copy the current directory contents into the container at /app
COPY . .

# run the migrations and application
CMD ["sh", "entrypoint.sh"]
