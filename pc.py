from logic import Pokemon
import random
import time
import asyncio

class PC:
    CPU = "AMD Ryzen 5 2600 6-Core Processor"
    GPU = "Radeon RX 570"
    RAM = "16GB"
    SSD_C = "224GB"
    SSD_D = "224GB"

    async def about_PC(self, ctx):
        await ctx.send(f"CPU: {self.CPU}, GPU: {self.GPU}, RAM: {self.RAM}, SSD C: {self.SSD_C}, SSD D: {self.SSD_D}")

    async def PC_status_discord(self, ctx):
        CPU_utilization = random.randint(0, 100)
        GPU_utilization = random.randint(0, 100)
        RAM_utilization = random.randint(0, 100)
        SSD_C_utilization = random.randint(0, 100)
        SSD_D_utilization = random.randint(0, 100)
        await ctx.send(f"CPU: {CPU_utilization}%, GPU: {GPU_utilization}%, RAM: {RAM_utilization}%, SSD C: {SSD_C_utilization}%, SSD D: {SSD_D_utilization}%")
        if any(x > 80 for x in [CPU_utilization, GPU_utilization, RAM_utilization, SSD_C_utilization, SSD_D_utilization]):
            await ctx.send("Uyarı: Yüksek kaynak kullanımı tespit edildi! PC performansını optimize etmek ister misiniz? (evet/hayır)")
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel
            try:
                msg = await ctx.bot.wait_for('message', check=check, timeout=30)
                if msg.content.lower() == "evet":
                    await ctx.send("PC performansı optimize ediliyor...")
                elif msg.content.lower() == "hayır":
                    await ctx.send("Optimizasyon yapılmayacak. Uzun süre yüksek kullanım donanım ömrünü kısaltabilir.")
                else:
                    await ctx.send("Geçersiz yanıt. Lütfen 'evet' veya 'hayır' yazınız.")
            except asyncio.TimeoutError:
                await ctx.send("Yanıt alınamadı, işlem iptal edildi.")
        else:
            await ctx.send("PC'niz optimal çalışıyor.")

    async def antivirus_scan_discord(self, ctx):
        await ctx.send("Antivirüs taraması yapılıyor...")
        scan_result = random.choice(["Tehdit bulunamadı.", "Tehditler tespit edildi!"])
        await ctx.send(scan_result)
        if scan_result == "Tehditler tespit edildi!":
            await ctx.send("Bu bir yanlış alarm mı? (evet/hayır)")
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel
            try:
                msg = await ctx.bot.wait_for('message', check=check, timeout=30)
                if msg.content.lower() == "evet":
                    await ctx.send("Yanlış pozitif olarak işaretlendi.")
                else:
                    await ctx.send("Potansiyel tehditler kaldırılıyor...")
            except asyncio.TimeoutError:
                await ctx.send("Yanıt alınamadı, işlem iptal edildi.")

    async def system_update_discord(self, ctx):
        await ctx.send("Güncellemeler kontrol ediliyor...")
        update_available = random.choice([True, False])
        if update_available:
            await ctx.send("Güncellemeler mevcut. Sistem güncellensin mi? (evet/hayır)")
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel
            try:
                msg = await ctx.bot.wait_for('message', check=check, timeout=30)
                if msg.content.lower() == "evet":
                    await ctx.send("Sistem güncelleniyor...")
                    await ctx.send("Sistem güncellendi.")
                else:
                    await ctx.send("Güncelleme atlandı.")
            except asyncio.TimeoutError:
                await ctx.send("Yanıt alınamadı, işlem iptal edildi.")
        else:
            await ctx.send("Sisteminiz güncel.")

    async def processes(self, ctx):
        processes = ["Visual Studio Code", "Google Chrome", "File Explorer"]
        bg_processes = ["AMD External Events Client Module", "AMD Crash Defender", "Windows Security Service"]
        msg = "Çalışan işlemler:\n" + "\n".join(processes) + "\nArka plan işlemleri:\n" + "\n".join(bg_processes)
        await ctx.send(msg)

    async def _sayi_tahmin_oyunu(self, ctx):
        await ctx.send("Sayı Tahmin Oyununa hoş geldin! 1-10 arasında bir sayı tuttum. 3 tahmin hakkın var.")
        number = random.randint(1, 10)
        
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        for guesses in range(3):
            try:
                await ctx.send(f"{3-guesses} hakkın kaldı. Tahminin nedir?")
                guess_msg = await ctx.bot.wait_for('message', check=check, timeout=20.0)
                guess = int(guess_msg.content)

                if guess < number:
                    await ctx.send("Daha yüksek bir sayı dene.")
                elif guess > number:
                    await ctx.send("Daha düşük bir sayı dene.")
                else:
                    points = 3 - guesses
                    Pokemon.pokepoints[ctx.author.name] = Pokemon.pokepoints.get(ctx.author.name, 0) + points
                    await ctx.send(f"🎉 Tebrikler! Doğru sayıyı ({number}) buldun ve {points} PokéPuan kazandın! Mevcut puanın: {Pokemon.pokepoints[ctx.author.name]}")
                    return
            except asyncio.TimeoutError:
                await ctx.send("Süre doldu! Oyunu kaybettin.")
                return

        await ctx.send(f"Maalesef bilemedin. Doğru sayı {number} idi.")

    async def _pokemon_trivia(self, ctx):
        await ctx.send("Pokémon Trivia oyununa hoş geldin!")

        questions = [
            {"soru": "Ash'in ilk Pokémon'u hangisidir?", "cevap": "pikachu"},
            {"soru": "Su Pokémon'ları Ateş Pokémon'larına karşı güçlü müdür? (evet/hayır)", "cevap": "evet"},
            {"soru": "Charmander'ın son evrimi nedir?", "cevap": "charizard"},
            {"soru": "Legendary Birds üçlüsünden buz türü olan hangisidir?", "cevap": "articuno"},
            {"soru": "Mewtwo hangi tür Pokémon'dur?", "cevap": "psikik"},
            {"soru": "Pokémon dünyasında en çok bilinen başlangıç Pokémon'u hangisidir?", "cevap": "bulbasaur"},
            {"soru": "Pokémon dünyasında en çok bilinen efsanevi Pokémon hangisidir?", "cevap": "mewtwo"},
            {"soru": "Pokémon dünyasında en çok bilinen su türü Pokémon hangisidir?", "cevap": "squirtle"},
            {"soru": "Pokémon dünyasında en çok bilinen elektrik türü Pokémon hangisidir?", "cevap": "pikachu"},
            {"soru": "Pokémon dünyasında en çok bilinen normal türü Pokémon hangisidir?", "cevap": "eevee"},
            {"soru": "Pokémon dünyasında en çok bilinen uçan türü Pokémon hangisidir?", "cevap": "pidgey"},
            {"soru": "Su Pokémon'ları Ateş Pokémon'larına karşı güçlü müdür? (evet/hayır)", "cevap": "evet"},
            {"soru": "Ash'in ilk Pokémon'u hangisidir?", "cevap": "pikachu"}
        ]
        
        question_data = random.choice(questions)
        await ctx.send(f"Soru: {question_data['soru']}")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await ctx.bot.wait_for('message', check=check, timeout=20.0)
            
            if msg.content.lower() == question_data['cevap']:
                points = 5
                Pokemon.pokepoints[ctx.author.name] = Pokemon.pokepoints.get(ctx.author.name, 0) + points
                await ctx.send(f"🎉 Doğru cevap! {points} PokéPuan kazandın! Mevcut puanın: {Pokemon.pokepoints[ctx.author.name]}")
            else:
                await ctx.send(f"Maalesef yanlış. Doğru cevap: **{question_data['cevap'].capitalize()}**")

        except asyncio.TimeoutError:
            await ctx.send("Süre doldu! Bu sorudan puan kazanamadın.")

    async def game(self, ctx):
        await ctx.send("Hangi oyunu oynamak istersin?\n"
                       "1. Sayı Tahmin Oyunu\n"
                       "2. Pokémon Trivia\n"
                       "Lütfen oynamak istediğin oyunun numarasını yaz.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content in ["1", "2"]

        try:
            choice_msg = await ctx.bot.wait_for('message', check=check, timeout=30.0)
            choice = choice_msg.content

            if choice == "1":
                await self._sayi_tahmin_oyunu(ctx)
            elif choice == "2":
                await self._pokemon_trivia(ctx)

        except asyncio.TimeoutError:
            await ctx.send("Oyun seçimi için süre doldu. Lütfen tekrar dene.")