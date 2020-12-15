Abstract:   
Abhay is an AI powered system to curb the spread of the SARS CoV-2 virus. It has been designed to effectively prevent the spread of the virus in the Trains and the Railway Stations.  The system is integration of 2-solutions to the problems being faced related to the transmission of the virus. Here we are focusing on the local trains of Mumbai. This system can also be implemented in other modes of transport. Through this system, people shall be able to travel in public transports without the fear of being infected due to negligence of other people not following social distancing protocols. The passengers shall be monitored by cameras powered by AI/ML. The key technical technologies used in the system are AI/ML, DBMS and IoT.
•	The first part of the system helps in better monitoring of the social distancing norms formulated to curb the transmission of SARS CoV-2 virus.
•	The second part of the system is a face recognition system, that can monitor one’s movement and if the person has his/her mask on.


Problem Statement:   
The major problems being faced in the current system of Railways are:
•	There is no proper tracking of the passengers entering the Railway Station 
•	There is no effective monitoring of the passengers, to check if they are adhering to the social distancing norms and whether everyone is wearing a mask at the Railway Station and inside the trains during the journey


Technical Report:   
The Abhay system works on the concepts of AI/ML, IoT and DBMS.
Usage of AI/ML: -
•	AI/ML will be used to detect the distance between two heads of passengers. If the distance is less than 3 feet, the loudspeaker will warn the person(s) to maintain social distancing norms.
•	It will also be used to detect the person’s face [1], match it with the records and identify if the mask is worn properly.
•	AI/ML will be used to train the face features of people, the ideal position of the mask on the face and the required distance between the heads.
Usage of IoT and DBMS: -
•	When the person enters the station, he scans QR code (on his ticket) / Smart Card. The image of the person shall be tagged with his/her Name, Train Number, and Ticket Number / Smart Card Number.
•	These details shall first be stored in the database of Railway Stations. This information shall be used in the waiting halls and platforms. 
•	The tagged entries shall then be sent to the trains’ database. All the entries sent to the trains’ database shall create a list of passengers who will be boarding the train. 
•	Trains database will keep check of the people entering the train. 
•	Any unauthorized entry detected will be informed to the nearest RPF post via an IoT trigger.  


Working:   
1.	Step-1: Person buys an online Ticket or Smart Card for the local train.
2.	Step-2: A unique QR code is sent to the person’s registered mobile number via WhatsApp (if the person has a Smart Card then this step will be skipped)
3.	Step-3: The person reaches the station and the QR code/ Smart card is scanned. The information (Name, Train Number in which he will be travelling) in the Smart Card/ QR code is stored in the database.
4.	Step-4: The person walks through a corridor, which has 4-smart cameras (AI enabled cameras), each placed on the top four corners of the corridor’s ceiling. The cameras capture the person from multiple angles and the images are tagged with his/her Name, Train Number, Ticket Number / Smart Card Number, and stored in the database.
5.	Step-5: The installed cameras will also check whether the person is wearing a mask. If the camera finds that, either there is no mask or not worn properly, then he/she will not be allowed to enter unless he wears the mask properly.
6.	Step-6: A copy of the same information of the person will also be uploaded on the train’s database (in which the person is going to travel).
7.	Step-7: The cameras will also be placed in waiting rooms and platforms. The cameras will take an image at regular interval of 2-minutes (which can be modified at the time of the setup). 
8.	Step-8: Then the images will be analyzed, and if it is found that that there are heads/people close to each other (< 3-feet), then face recognition system shall identify the person and will send a trigger for a loudspeaker announcement for the identified person(s) to follow the norms.
9.	Step-9: When the train arrives at destination station, the person scans the QR code/ Smart Card. If the Smart Card/QR Code is not scanned or an unauthorized Smart Card/QR Code is scanned, the nearest RPF post will be informed via an IoT trigger.
10.	Step-10: The cameras in the train compartment will also scan people and their faces to check if norms are being violated. The same rule implies here. If the norms are broken more than three times, then the person’s ticket shall be immediately confiscated and while deboarding they will be asked to pay the fine. 


