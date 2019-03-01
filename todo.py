from flask import Flask, jsonify,abort,request
app=Flask(__name__)
app.debug=True

todo_items=[
    {
        "id":1,
        "title":"Do this excercise",
        "description":"In-class work",
        "complete":False
    }
]
@app.route('/')
def main():
    return jsonify({"message":"OK"})

@app.route('/todo/items',methods=['GET'])
def getall():
    return jsonify({"items":todo_items})

@app.route('/todo/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    for task in todo_items:
        if task['id']==task_id:
            return jsonify({"task":task})
    abort(404)

@app.route('/todo/tasks',methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    title=request.json['title']
    description=request.json.get('description','')
    done=False
    new_id=0
    if len(todo_items)<=0:
        new_id==1
    elif len(todo_items)!=0:
        new_id=todo_items[-1]['id']+1
    todo_items.append({
        "id":new_id,
        "title":title,
        "description":description,
        "complete":done

    })
    return jsonify({"task":todo_items[-1]})

@app.route('/todo/tasks/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in todo_items if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:        
        abort(400)
    if 'title' not in request.json:       
        abort(400)
    if 'description' not in request.json:
        abort(400)
    if 'complete' not in request.json:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['complete'] = request.json.get('complete', task[0]['complete'])
    return jsonify({'task': task[0]})

@app.route('/todo/tasks/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in todo_items if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    todo_items.remove(task[0])
    return jsonify({'result': True})



if __name__=="__main__":
    app.run()
    