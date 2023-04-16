# Creates app
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Specifying to ensure the right input from requests
class model_input(BaseModel):
   
   zipcode: int
   lot_len: float
   lot_area: int
   house_area:int
   garden_size: int
   y_coor: int
   energy_eff: int
   
   # loading the saved model
model = pickle.load(open('model.pkl', 'rb'))

@app.post('/house_prediction')
def house_predd(input_parameters : model_input):

    input_data = input_parameters.json()
    # Converts to dict
    input_dictionary = json.loads(input_data)
    
    # Gets the values of the keys
    zip = input_dictionary['zipcode']
    lotl= input_dictionary['lot_len']
    lota= input_dictionary['lot_area']
    house= input_dictionary['house_area']
    garden= input_dictionary['garden_size']
    y_coor = input_dictionary['y_coor']
    eff = input_dictionary['energy_eff']

    input_list = [zip, lotl, lota, house, garden, y_coor, eff]    
    # Use saved model to predict
    prediction = model.predict([input_list])

    return prediction[0]

ngrok_tunnel = ngrok.connect(8000)
# Gets public url
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
