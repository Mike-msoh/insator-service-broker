import insator_plans
import uuid

# Service

def insatorsvc():
	insator_service_id = '27a50a28-42ab-47e6-a7c6-e8066d8dcaa1' # Generate unique service ID
	insator_service = { 
         "bindable":True,
         "dashboard_client":{  
            "id":"insator-broker-dashboard-4832-a349-48b0ca350171",
            "redirect_uri":"http://localhost:1234",
            "secret":"86874ff3-dc02-45c1-baea-edcaa666e891"
         },
         "description":"Enterprise IoT platform by Samsung SDS",
         "id":"insator-service-a9a4-2c16ae2eec90",
         "tags":[
            "internet_of_things",
            "ibm_third_party"
         ],
         "max_db_per_node":5,
         "metadata":{  
            "displayName":"Insator",
            "embeddableDashboard":True,
            "provider":{  
               "name":"Samsung SDS"
            },
            "longDescription":"Accumulate and analyze useful data on our verified, enterprise-wide common platform. Insator connects to IoT devices, extracts data, and offers insightful conclusions that can reshape your business operations.",
            "termsUrl":"https://iot.insator.io/web/est/index.html#/signUp",
            "media":[
               {
                  "type":"image",
                  "url":"https://sds-insator-ui-service.mybluemix.net/image/catalog/image0.png",
                  "thumbnailUrl":"https://sds-insator-ui-service.mybluemix.net/image/catalog/image0.png",
                  "caption":"Samsung SDS"
               },
               {
                  "type":"image",
                  "url":"https://sds-insator-ui-service.mybluemix.net/image/catalog/image1.png",
                  "thumbnailUrl":"https://sds-insator-ui-service.mybluemix.net/image/catalog/image1.png",
                  "caption":"Samsung SDS"
               },
               {
                  "type":"youtube",
                  "thumbnailUrl":"https://img.youtube.com/vi/Fi2uU8f1Ngc/0.jpg",
                  "url":"https://www.youtube.com/embed/Fi2uU8f1Ngc",
                  "caption":"Samsung SDS"
               },
               {
                  "type":"youtube",
                  "thumbnailUrl":"https://img.youtube.com/vi/Z1boU00135o/0.jpg",
                  "url":"https://www.youtube.com/embed/Z1boU00135o",
                  "caption":"Samsung SDS"
               }
            ],
            "bullets":[  
               {  
                  "title":"Easily connect your IoT devices",
                  "description":"The protocol adapter allows this intelligent open platform to seamlessly connect with IoT devices using MQTT, CoAP, and WebSocket protocols. With an SDK that supports C, Java, .Net, Android and iOS, InsatorTM is compatible with various languages and protocols. "
               },
               {  
                  "title":"Securely manage IoT devices ",
                  "description":"All connected IoT devices can be securely managed with numerous authentication methods including SEAL, OAuth, DH-based key exchange, and SSL. Additional encryption keys are locked in the Key Management System, providing end-to-end security. "
               },
               {  
                  "title":"Insightfully discover your business value ",
                  "description":"All data collected by your IoT devices converge with InsatorTM to deliver precise and reliable results. Use our time-proven and verified platform and reduce lead times by forgoing the architecture verification process. Spend more time building your business. "
               },
               {  
                  "title":"Conveniently centralize your data for analytics ",
                  "description":"InsatorTM quickly gathers and organizes your data, including DB, File, Log, Legacy-data, and External-data. It allows our BrighticsTM solution to interpret data collections and turn them into intuitive visual representations to give you the full picture. "
               }

            ],

            "serviceKeysSupported":False,
            "imageUrl":"https://sds-insator-ui-service.mybluemix.net/image/catalog/Iot-Connectivity_50.png",
            "smallImageUrl":"https://sds-insator-ui-service.mybluemix.net/image/catalog/Iot-Connectivity_24.png",
            "mediumImageUrl":"https://sds-insator-ui-service.mybluemix.net/image/catalog/Iot-Connectivity_32.png",
            "featuredImageUrl":"https://sds-insator-ui-service.mybluemix.net/image/catalog/Iot-Connectivity_64.png",
            "documentationUrl":"https://sds-insator-ui-service.mybluemix.net/image/guide.html"
         },
         "name":"SDS-insator-auth-service",
         "plan_updateable":False,
         "plans":[ 
            {  
               "name":"free-plan",
               "description":"Free plan",
               "free" : True,
               "id":"sds-insator-plan-8846-f17cefcfb6b4",
               "metadata":{  
                  "asyncProvisioningSupported":False,
                  "bullets":[  
                    "TBD"
                  ],
                  "costs":[  
                      { 
                         "unit":"MONTHLY"   
                      } 
                  ]
               }
            }
         ],
         "requires":[  
            "route_forwarding"
         ]
      }
	return insator_service
