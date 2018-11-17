from flask import Flask, request, render_template
from flask_cors import CORS

#initiallize app and take care of cross orogin resource
app = Flask(__name__)
CORS(app)

#initialize our counter to zero, ref to gloal
counter = 0
food_item = []
# food_dict = {
# 	'Ghio-Krob': 'spicy fried won-ton with potato, onion and curry powder, served with cool, refreshing cucumber sauce', 
# 	'Tom-Yum': 'choice of chicken or prawns*, served with mushroom and lemon grass, in a lime juice hot-n-sour broth',
# 	'Kang-Curry': 'chicken simmered in yellow curry, with coconut milk, potatoes and carrots',
# 	'Thai-Suki':'crystal bean thread noodles with beef, chicken, prawns, calamari, fish balls, bean curd and eggs cooked with a variety of vegetables in a special soy bean sauce'
# }
food_dict = {
	'hawaiian tuna crunch roll': 'tuna, pickled red onion, habanero, mango, turmeric almonds, cilantro, eel sauce',
	'naruto roll':'tuna, yellowtail, salmon, spring mix, avocado, cucumber wrapper, yuzu ponzu, togarashi, sriracha',
	'dragon roll':'crab mix, motoyaki sauce, cucumber, eel, eel sauce',
	'sunshine roll':'salmon & spicy sesame sauce, cucumber, salmon, shaved lemon',
	'voodoo roll':'spicy crawfish, fresh avocado, tuna, habanero sauce, green onion, smelt roe',
	'caterpillar roll':'eel, cucumber, avocado, eel sauce',
	'checkerboard roll':'habanero tuna, fresh avocado, asparagus, tuna, yellowtail, spicy motoyaki sauce',
	'rainbow roll':'california roll, tuna, salmon, shrimp, yellowtail',
	'flamingo roll':'salmon, lemon, spicy crab mix, fresh avocado, chili-sriracha sauce, yuzu ponzu, asparagus, cucumber, green onion, smelt roe',
	'spider roll':'soft shell crab deep fried, crab mix, fresh avocado, cucumber, nori & soy paper, eel sauce',
	'philadelphia roll':'smoked salmon, cream cheese, cucumber',
	'california roll':'crab mix, motoyaki sauce, cucumber, fresh avocado',
}

recommend = []
#func decorator operate in a specific was

@app.route('/')
def index():
	return render_template('index.html')

#client send get req to counter server
@app.route('/counter', methods=['GET'])
def get_counter():
    global counter
    return str(counter),200 #status code

@app.route('/item', methods=['POST'])
def get_item():
	txt = request.form['field1']
	print(txt)
	global food_item
	food_item.append(txt)
	print(food_item)
	return str(food_item),200 #status code

@app.route('/add', methods=['POST'])
def add_1():
    global counter
    counter += 1
    return '', 200

@app.route('/search', methods=['POST'])
def search_meals():
	global food_item, food_dict, recommend, counter
	counter = 0
	for k in food_dict:
		if all([f in food_dict[k] for f in food_item]):
			print(k)
			#return render_template('index.html', food=k)
	# for k in food_dict:
	# 	if all([food in food_dict for food in food_item])
	#     for food in food_item:
	#     	if food in food_dict[k]:
	#     		if k not in recommend:
	# 	    		recommend.append(k)
	# [print(r) for r in recommend]
	# food_item = []
	#return '', 200

	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

