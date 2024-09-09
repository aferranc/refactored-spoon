## 1.4.0 (2024-09-09)

### Feat

- Register main blueprint
- Register authentication blueprint
- Initialize blueprints
- Configure flask application factory

### Fix

- Fix blueprint configuration
- Move errors templates to blueprint directory
- Ignore all log files
- Rename FLASK_APP file

### Refactor

- Remove 'Remeber me' checkbox

## 1.3.1 (2024-09-09)

### Refactor

- Set Catalan as default language
- Add Catalan tex translations

## 1.3.0 (2024-09-09)

### Feat

- Generated Spanish language catalogue and translations
- Add command cli to manage translations more easily
- Configure and adapt templates to show translated texts
- Initial babel configuration
- Add flask-babel package

### Fix

- Move the configuration file to top directory

### Refactor

- Remove language translations

## 1.2.1 (2024-09-08)

### Fix

- Add flash message status category
- Show flash messages based on status category
- Remove function

### Refactor

- Set logging to file in production mode
- Configure 404 and 500 error handlers
- enable trim_trailing_whitespace and insert_final_newline
- Remove empty end line

## 1.2.0 (2024-09-08)

### Feat

- Add login and logut pages

### Fix

- Fix tables relationships

### Refactor

- Adapt templates to tables fix

## 1.1.4 (2024-09-08)

### Fix

- Add sqlite stuff
- Add config file
- User login using flask-login
- Add FLASK_APP main script

### Refactor

- Add restaurant tables and relationships
- Add python-dotenv devel package
- Add flask-wtf package

## 1.1.3 (2024-09-08)

### Refactor

- Serve css scripts locally
- Set version number on js files
- Split functions into separate files
- Serve js scripts locally

## 1.1.2 (2024-09-08)

### Fix

- Add top margin to flash messages

### Refactor

- Comment pdm files

## 1.1.1 (2024-09-08)

### Fix

- Add admin login

### Refactor

- Rename app directory name
- Adapt to the new structure
- Add html base layouts
- Add EditorConfig file
- Add navigation bar

## 1.1.0 (2024-09-08)

### Feat

- Add admin login feature and create new Users table

### Fix

- Remove /create_user route

## 1.0.0 (2024-09-07)

### BREAKING CHANGE

- From now on you can edit the information of a restaurant

### Feat

- **frontend**: Add edit restaurant template
- **frontend**: Add edit restaurant route
- **custom.jss**: Hide flash message after 5 seconds
- **custom.jss**: Configured info layout and translated some phrases

## 0.2.0 (2024-09-07)

### Feat

- Add datatables css and js
- Add table order

### Fix

- Remove th to avoid conflicts

### Refactor

- Remove BUILD_DIR variable
- Configure commitizen tool
- Export requirements.txt file
