from flask import Flask, render_template

app = Flask(__name__)

# Produse cu imagini de pe internet
produse = [
    {
        "nume": "Gem de Zmeură",
        "pret": 18,
        "imagine": "https://savoriurbane.com/wp-content/uploads/2020/06/Gem-de-zmeur%C4%83-f%C4%83r%C4%83-conservan%C8%9Bi-cu-pu%C8%9Bin-zah%C4%83r-reteta-savori-urbane.jpg",
        "descriere": "Din zmeură proaspătă culeasă din grădină"
    },
    {
        "nume": "Gem de Caise",
        "pret": 16,
        "imagine": "https://www.lauralaurentiu.ro/wp-content/uploads/2009/07/gem-de-caise-reteta-cum-se-face-gem-de-caise-pentru-iarna-reteta-laura-laurentiu.jpg",
        "descriere": "Dulce-acrișor, ca la mama acasă"
    },
    {
        "nume": "Gem de Afine",
        "pret": 20,
        "imagine": "https://savoriurbane.com/wp-content/uploads/2020/07/Gem-de-afine-re%C8%9Beta-tradi%C8%9Bional%C4%83-savori-urbane.jpg",
        "descriere": "Aromă de pădure, 100% natural"
    }
]

@app.route('/')
def home():
    return render_template('index.html', produse=produse)

if __name__ == '__main__':
    app.run(debug=True)