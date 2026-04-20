from app.core.firebase import db

products = [

    # =========================
    # 🧶 YARN & THREAD (10)
    # =========================
    {
        "id": "P001",
        "name": "Merino Yarn Roll",
        "price": 499,
        "category": "Yarn",
        "image": "assets/card/yarn.jpeg",
        "description": "Premium Merino wool yarn, soft and perfect for knitting."
    },
    {
        "id": "P002",
        "name": "Hand-Spun Yarn Bundle",
        "price": 699,
        "category": "Yarn",
        "image": "assets/card/yarns.jpeg",
        "description": "Traditional Indian hand-spun wool thread from farm sources."
    },
    {
        "id": "P003",
        "name": "Winter Knitting Yarn Pack",
        "price": 799,
        "category": "Yarn",
        "image": "assets/card/yarns.jpeg",
        "description": "Thick wool yarn pack best for sweaters and blankets."
    },
    {
        "id": "P004",
        "name": "Soft Alpaca Yarn",
        "price": 899,
        "category": "Yarn",
        "image": "assets/card/yarn.jpeg",
        "description": "Warm alpaca blend yarn, silky and lightweight."
    },
    {
        "id": "P005",
        "name": "Cashmere Yarn Set",
        "price": 1299,
        "category": "Yarn",
        "image": "assets/card/yarns.jpeg",
        "description": "Luxury cashmere yarn for premium garments."
    },
    {
        "id": "P006",
        "name": "Mohair Blend Thread",
        "price": 999,
        "category": "Yarn",
        "image": "assets/card/yarn.jpeg",
        "description": "Strong mohair fiber thread with glossy finish."
    },
    {
        "id": "P007",
        "name": "Eco Wool Yarn Roll",
        "price": 599,
        "category": "Yarn",
        "image": "assets/card/yarn.jpeg",
        "description": "Sustainably produced wool yarn from verified farms."
    },
    {
        "id": "P008",
        "name": "Crochet Wool Thread",
        "price": 399,
        "category": "Yarn",
        "image": "assets/card/yarns.jpeg",
        "description": "Fine wool thread for crochet and detailed work."
    },
    {
        "id": "P009",
        "name": "Multi-Color Yarn Pack",
        "price": 749,
        "category": "Yarn",
        "image": "assets/card/yarns.jpeg",
        "description": "Colorful wool yarn bundle for stylish crafts."
    },
    {
        "id": "P010",
        "name": "Blanket Yarn Heavy Roll",
        "price": 899,
        "category": "Yarn",
        "image": "assets/card/yarn.jpeg",
        "description": "Extra thick wool yarn designed for blankets and rugs."
    },


    # =========================
    # 👕 GARMENTS (10)
    # =========================
    {
        "id": "P011",
        "name": "Classic Wool Sweater",
        "price": 1999,
        "category": "Garments",
        "image": "assets/card/sweater.jpeg",
        "description": "Warm everyday wool sweater for winter use."
    },
    {
        "id": "P012",
        "name": "Red Wool Sweater Premium",
        "price": 2199,
        "category": "Garments",
        "image": "assets/card/redsweater.jpeg",
        "description": "Premium red sweater made with high-grade wool."
    },
    {
        "id": "P013",
        "name": "Blue Wool Sweatshirt",
        "price": 1899,
        "category": "Garments",
        "image": "assets/card/bluesweatshirt.jpeg",
        "description": "Soft wool blend sweatshirt for casual winter wear."
    },
    {
        "id": "P014",
        "name": "Heavy Winter Wool Coat",
        "price": 3499,
        "category": "Garments",
        "image": "assets/card/coat.jpeg",
        "description": "Long wool coat designed for extreme cold climates."
    },
    {
        "id": "P015",
        "name": "Wool Dress Collection",
        "price": 2799,
        "category": "Garments",
        "image": "assets/card/dress.jpeg",
        "description": "Stylish wool dress for both comfort and warmth."
    },
    {
        "id": "P016",
        "name": "Merino Wool Beanie",
        "price": 499,
        "category": "Garments",
        "image": "assets/card/beanie.jpeg",
        "description": "Soft Merino cap for daily winter protection."
    },
    {
        "id": "P017",
        "name": "Wool Gloves Set",
        "price": 599,
        "category": "Garments",
        "image": "assets/card/gloves.jpeg",
        "description": "Comfortable gloves for warmth and grip."
    },
    {
        "id": "P018",
        "name": "Wool Scarf Wrap",
        "price": 699,
        "category": "Garments",
        "image": "assets/card/scarfs.jpeg",
        "description": "Long wool scarf for travel and winter fashion."
    },
    {
        "id": "P019",
        "name": "Thermal Wool Socks Pack",
        "price": 399,
        "category": "Garments",
        "image": "assets/card/socks.jpeg",
        "description": "Thick wool socks for cold weather comfort."
    },
    {
        "id": "P020",
        "name": "Wool Winter Shoes",
        "price": 2499,
        "category": "Garments",
        "image": "assets/card/shoes.jpeg",
        "description": "Wool-lined shoes for warm winter walking."
    },


    # =========================
    # 🏠 HOME TEXTILES (10)
    # =========================
    {
        "id": "P021",
        "name": "Premium Wool Blanket",
        "price": 2499,
        "category": "Home",
        "image": "assets/card/blanket.jpg",
        "description": "Soft wool blanket providing excellent insulation."
    },
    {
        "id": "P022",
        "name": "Double Layer Blanket",
        "price": 2799,
        "category": "Home",
        "image": "assets/card/blanket2.jpeg",
        "description": "Extra warm wool blanket for cold nights."
    },
    {
        "id": "P023",
        "name": "Wool Bedsheet Set",
        "price": 1599,
        "category": "Home",
        "image": "assets/card/bedsheet.jpeg",
        "description": "Cozy wool-blend bedsheet for winter comfort."
    },
    {
        "id": "P024",
        "name": "Luxury Bedsheet Pack",
        "price": 1799,
        "category": "Home",
        "image": "assets/card/Bedsheet2.jpeg",
        "description": "Premium wool textile bedsheets with soft finish."
    },
    {
        "id": "P025",
        "name": "Designer Bedsheet Collection",
        "price": 1899,
        "category": "Home",
        "image": "assets/card/bedsheet3.jpeg",
        "description": "Modern wool texture bedsheets with elegant look."
    },
    {
        "id": "P026",
        "name": "Wool Towels Set",
        "price": 999,
        "category": "Home",
        "image": "assets/card/towels.jpeg",
        "description": "High absorbent wool blend towel pack."
    },
    {
        "id": "P027",
        "name": "Handmade Wool Carpet",
        "price": 3999,
        "category": "Home",
        "image": "assets/card/Carpet.jpeg",
        "description": "Durable handmade wool carpet for home interiors."
    },
    {
        "id": "P028",
        "name": "Premium Carpet Edition",
        "price": 4499,
        "category": "Home",
        "image": "assets/card/Carpet2.jpeg",
        "description": "Thick premium carpet for halls and lounges."
    },
    {
        "id": "P029",
        "name": "Large Carpet Design",
        "price": 4999,
        "category": "Home",
        "image": "assets/card/Carpet3.jpeg",
        "description": "Luxury woven wool carpet for large living rooms."
    },
    {
        "id": "P030",
        "name": "Royal Carpet Collection",
        "price": 5999,
        "category": "Home",
        "image": "assets/card/Carpet5.jpeg",
        "description": "High-end wool carpet with premium finish."
    },


    # =========================
    # 🧺 UTILITY & ACCESSORIES (10)
    # =========================
    {
        "id": "P031",
        "name": "Wool Door Mat",
        "price": 799,
        "category": "Utility",
        "image": "assets/card/DoorMat.jpeg",
        "description": "Strong wool mat for indoor and outdoor entrances."
    },
    {
        "id": "P032",
        "name": "Storage Wool Basket",
        "price": 899,
        "category": "Utility",
        "image": "assets/card/baskets.jpeg",
        "description": "Handwoven wool basket for eco-friendly storage."
    },
    {
        "id": "P033",
        "name": "Classic Wool Shoes",
        "price": 2599,
        "category": "Utility",
        "image": "assets/card/shoes2.jpeg",
        "description": "Soft premium wool shoes for daily winter comfort."
    },
    {
        "id": "P034",
        "name": "Sport Wool Shoes",
        "price": 2699,
        "category": "Utility",
        "image": "assets/card/shoes3.jpeg",
        "description": "Modern wool shoes built for style and warmth."
    },
    {
        "id": "P035",
        "name": "Traditional Wool Shawl",
        "price": 1499,
        "category": "Utility",
        "image": "assets/card/shawl2.jpeg",
        "description": "Soft wool shawl wrap for winter travel."
    },
    {
        "id": "P036",
        "name": "Premium Carpet Round Mat",
        "price": 3299,
        "category": "Utility",
        "image": "assets/card/carpet4.jpeg",
        "description": "Decorative wool mat for premium interiors."
    },
    {
        "id": "P037",
        "name": "Extra Large Hall Carpet",
        "price": 6999,
        "category": "Utility",
        "image": "assets/card/Carpet6.jpeg",
        "description": "Large wool carpet made for halls and wide spaces."
    },
    {
        "id": "P038",
        "name": "Winter Gift Basket Pack",
        "price": 1099,
        "category": "Utility",
        "image": "assets/card/baskets.jpeg",
        "description": "Eco wool-woven gift basket for festive season."
    },
    {
        "id": "P039",
        "name": "Luxury Wool Carpet Set",
        "price": 7999,
        "category": "Utility",
        "image": "assets/card/Carpet2.jpeg",
        "description": "Premium multi-room wool carpet bundle."
    },
    {
        "id": "P040",
        "name": "Wool Comfort Floor Mat",
        "price": 999,
        "category": "Utility",
        "image": "assets/card/DoorMat.jpeg",
        "description": "Soft wool mat for bedroom and indoor spaces."
    },
]

# ✅ Push into Firestore
for p in products:
    db.collection("products").document(p["id"]).set(p)

print("✅ Seeded 40 products successfully!")