#/path/path/
#title           :AWS SQS Class
#description     :AWS SQS services.
#update date     :01/01/2020 12:10
#version         :1.0
#changes         :veriosn 1.0.
#python_version  :3.6  
#==============================================================================

import boto3
import json

class Sqs():
    # constructor
    def __init__(self, sqs_name):
        self.__sqs   = boto3.resource('sqs')

        try:
            self.__queue = self.__sqs.get_queue_by_name(QueueName=sqs_name)
        except:
            raise Exception("queue doesn't exist")


    # getter and setter of new queue
    @property
    def queue(self):
        return self.__queue.url

    @queue.setter
    def queue(self, new_queue):
            try:
                self.__queue = self.__sqs.get_queue_by_name(QueueName=new_queue)
            except:
                raise Exception("queue doesn't exist")
            return True


    # receive message from SQS queue
    def receive_messages(self):
        try:
            messages = self.__queue.receive_messages()

            if len(messages) == 0:
                raise Exception("sqs queue is empty")

        except Exception as ex:
            raise ex
        return messages


    # send message from SQS queue
    # message body type = dict
    def send_messages(self, message_body):
        try:
            messages_id = self.__queue.send_message(MessageBody=json.dumps(message_body))
        except Exception as ex:
            raise ex

        return messages_id


    # delete message from SQS queue
    def delete_message(self, message):
        try:
            message.delete()
        except Exception as ex:
            raise ex
        return True


    # purge queue - remove all message from the queue
    def purge_queue(self):
        try:
            self.__queue.purge()
        except Exception as ex:
            raise ex
        return True