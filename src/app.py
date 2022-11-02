from flask import Flask, request, jsonify

app = Flask(__name__)

list_books = [
  {
    'id':1,
    'author':'autor 1',
    'language':'lan 1',
    'title':'T 1'
  },
  {
    'id':2,
    'author':'autor 2',
    'language':'lan 2',
    'title':'T 2'
  },
  {
    'id':3,
    'author':'autor 3',
    'language':'lan 3',
    'title':'T 3'
  },
  {
    'id':4,
    'author':'autor 4',
    'language':'lan 4',
    'title':'T 4'
  },
  {
    'id':5,
    'author':'autor 5',
    'language':'lan 5',
    'title':'T 5'
  },
  {
    'id':6,
    'author':'autor 6',
    'language':'lan 6',
    'title':'T 6'
  }
]

global_obj = {
  'message':'libros',
  'data':list_books
  }


@app.route('/books', methods=['GET','POST'])
def books():
  if request.method == 'GET':
    return global_obj, 200

  if request.method == 'POST':
    new_author = request.form['author']
    new_language = request.form['language']
    new_title = request.form['title']
    ID_list = list_books[-1]['id'] + 1

    new_obj = {
      'id':ID_list,
      'author':new_author,
      'language':new_language,
      'title':new_title
    }

    list_books.append(new_obj)
    return global_obj, 200


@app.route('/books/<int:id>', methods = ['GET','POST','DELETE'])
def work_one(id):
  choosed_obj=0
  position = 0
  for obj in list_books:
    if obj['id'] == id:
      choosed_obj = obj
  
  if request.method == 'GET':
    return choosed_obj

  if request.method == 'DELETE':
    for index, book in enumerate(list_books):
      if(book['id'] ==id):
        list_books.pop(index)
        break
    return list_books

#THIS SOLUTIONS WORKS, AND THE OTHER TOO
  # if request.method == 'DELETE':
  #   for obj in list_books:
  #     if obj['id'] == id:
  #       break
  #     position = position + 1
  #   list_books.pop(position)
  #   return list_books

@app.route('/')
def home():
  return "hola"
















app.run(debug=True)