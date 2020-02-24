def game_ftbl():
    if request.method == 'GET':

# show html form
        return '''
            <form method="post">
                <input type="submit" name="A" value='Get 1'/>
                <input type="submit" name="A" value='Get 2'/>
            </form>
        '''
#run script
    elif request.method == 'POST':
        if request.form['A'] == 'Get 1':
            return '1'
        elif request.form['A'] == 'Get 2':
            return '2'
