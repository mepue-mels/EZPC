from sql import create_server_connection
from user import User
from handler import Handler

conn = create_server_connection('localhost', 'root', 'Mar2022100306')

sample = User()
sample.setCredentials("root", "root")

handlerTest = Handler(sample, conn)

deleteUser = handlerTest.deleteUser("test", "test")

print(deleteUser)
