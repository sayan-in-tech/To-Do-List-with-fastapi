    (app-user)
UserEntity {
	long id
	string username
	string password
}

(tasks)
TaskEntity {
	long id
	string title
	string description
	UserEntity user // foriegn key, many to one
}

API:

user DTO 

create example 

POST at /api/create

UserCreateRequestModel {
	string username
	string password
}

UserCreateResponseModel {
	string username
	string password
}

Response (status code mandatory)

ResponseModel
{
	data: {
		
	},
	error: { // optional
		errorCode: string,
		errorDescription: string
	},
	additionalParams: {
		"keyX": "valueX"
	}
}


* put exception handling in service layer,
* in case of exception, get the type and message of exception
  and use it to populate responseModel properly (error)
* (optional) return a response model also for not supported URIs