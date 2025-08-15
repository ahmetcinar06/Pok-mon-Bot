import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random

class Pokemon:
    pokemons = {}
    pokepoints = {}

    legendary = ["Mew", "Mewtwo", "Rayquaza"]
    epic = ["Yveltal", "Zygarde", "Darkrai"]
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.abilities = []
        self.types = []
        self.image_url = None
        self._data_fetched = False # Verilerin API'den çekilip çekilmediğini kontrol eden bayrak
        Pokemon.pokemons[pokemon_trainer] = self
        if pokemon_trainer not in Pokemon.pokepoints:
            Pokemon.pokepoints[pokemon_trainer] = 0

    async def _fetch_data(self):
        # Veriler zaten çekilmişse tekrar istek göndermeyi engelle
        if self._data_fetched:
            return

        # PokeAPI aracılığıyla pokémon verilerini almak için asenkron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    self.name = data['name'].capitalize()
                    self.abilities = [a['ability']['name'].capitalize() for a in data['abilities']]
                    self.types = [t['type']['name'].capitalize() for t in data['types']]
                    self.image_url = data['sprites']['front_default']
                else:
                    # İstek başarısız olursa varsayılan değerleri ata
                    self.name = "Pikachu"
                    self.abilities = ["Static"]
                    self.types = ["Electric"]
                    self.image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
                self._data_fetched = True

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        await self._fetch_data() # Verilerin yüklendiğinden emin ol

        # Özel bir pokémon (örn: Mew) geldiğinde farklı bir mesaj göster
        if self.name.lower() in Pokemon.legendary:
            Pokemon.pokepoints[self.pokemon_trainer] += 10
            return (f"🎉 Vay canına, {self.pokemon_trainer}! Çok şanslısın! {self.name} adlı efsanevi Pokémon'u buldun! 🎉\n"
                    f"**Türleri:** {', '.join(self.types)}\n"
                    f"**Yetenekleri:** {', '.join(self.abilities)}\n"
                    f"+10 PokéPoint aldın! Toplam {Pokemon.pokepoints[self.pokemon_trainer]} PokéPoint'un var.")

        elif self.name.lower() in Pokemon.epic:
            Pokemon.pokepoints[self.pokemon_trainer] += 5
            return (f"Vay canına, {self.pokemon_trainer}! Çok şanslısın! {self.name} adlı epik Pokémon'u buldun! 🎉\n"
                    f"**Türleri:** {', '.join(self.types)}\n"
                    f"**Yetenekleri:** {', '.join(self.abilities)}\n"
                    f"+5 PokéPoint aldın! Toplam {Pokemon.pokepoints[self.pokemon_trainer]} PokéPoint'un var.")

        # Standart bilgi mesajı
        else:
            Pokemon.pokepoints[self.pokemon_trainer] += 1
            return (f"İşte Pokémon'un, **{self.name}**!\n"
                    f"**Türleri:** {', '.join(self.types)}\n"
                    f"**Yetenekleri:** {', '.join(self.abilities)}\n"
                    f"+1 PokéPoint aldın! Toplam {Pokemon.pokepoints[self.pokemon_trainer]} PokéPoint'un var.")

    async def show_img(self):
        # Pokémon'un resim URL'sini döndürür
        await self._fetch_data() # Verilerin yüklendiğinden emin ol
        return self.image_url