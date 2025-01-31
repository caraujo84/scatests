# for gmail
import base64
import datetime
import os.path
import pathlib
import pickle
import time

from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class Gmail:
    """
    The gmail class connects to the Gmail API by
    providing credentials to the site and then bring
    the required information. You can use several parameters
    to get the emails that you want. It will return them
    as html strings.

    Methods
    -------
    __init__
        Constructor of the class.
    search_messages
        Method to retrieve emails from the API using operators.
    search_messages_by_subject_and_receiver
        Passes the subject and receiver email as parameters to search_messages method.
    """

    def __init__(self, log):
        """Constructor"""
        self.user_id = "me"
        self.log = log
        self.service = self.__get_service()

    def search_message_by_operator(self, operator, element_to_find, date=True):
        """Allows to look for emails using an operator.

        Parameters
        ----------
        operator : str,
            can be: 'subject', 'from', 'to',
             'before' (get last email before a certain M/D/YYYY date format).
        element_to_find : str,
            can be the text of the subject, email of sender or receiver, and dates.
        date : bool, optional:
            True > to check only today's emails
             | False > to check in all emails

        Returns
        -------
        str,
            HTML of the email if found, else None.
        """
        search_string = (
            operator
            + ":"
            + element_to_find
            + " after:"
            + str(datetime.date.today()).replace("-", "/")
            if date
            else operator + ":" + element_to_find
        )
        email_html = self.__search_messages(search_string)
        if email_html != None:
            return email_html
        else:
            self.log.warning("Email not found on INBOX. Trying to find it on SPAM ...")
            email_html = self.__search_message_by_operator_in_spam(
                operator, element_to_find, date=True
            )
            return email_html

    def __search_message_by_operator_in_spam(
        self, operator, element_to_find, date=True
    ):
        """Allows to look for emails using an operator.

        Parameters
        ----------
        operator : str,
            can be: 'subject', 'from', 'to',
             'before' (get last email before a certain M/D/YYYY date format).
        element_to_find : str,
            can be the text of the subject, email of sender or receiver, and dates.
        date : bool, optional:
            True > to check only today's emails
             | False > to check in all emails

        Returns
        -------
        str,
            HTML of the email if found, else None.
        """
        search_string = (
            operator
            + ":"
            + element_to_find
            + " after:"
            + str(datetime.date.today()).replace("-", "/")
            if date
            else operator + ":" + element_to_find
        )
        email_html = self.__search_messages(search_string, labelId="SPAM")
        return email_html

    def __search_messages_by_subject_and_receiver_in_spam(
        self, subject_text, receiver_email, date=True
    ):
        """Method used to find an email by its subject and receiver but in the SPAM folder.

        Parameters
        ----------
        subject_text : str,
            text of the subject in email.
        receiver_email : str,
            email address of the receiver.
        date : bool, optional
            True > to check only today's emails
            | False > to check in all emails

        Returns
        -------
        str,
            HTML of the email if found, else None.
        """
        search_string = (
            "subject:"
            + subject_text
            + " "
            + "to:"
            + receiver_email
            + " after:"
            + str(datetime.date.today()).replace("-", "/")
            if date
            else "subject:" + subject_text + " " + "to:" + receiver_email
        )
        email_html = self.__search_messages(search_string, labelId="SPAM")
        return email_html

    def search_messages_by_subject_and_receiver(
        self, subject_text, receiver_email, date=True
    ):
        """Allows to get an email using the 'subject' and 'to' operators in query.

        Parameters
        ----------
        subject_text : str,
            text of the subject in email
        receiver_email : str,
            email address of the receiver.
        date : bool,
             True > to check only today's emails
             | False > to check in all emails

        Returns
        -------
        string,
            HTML of the email if found, else None.
        """
        search_string = (
            "subject:"
            + subject_text
            + " "
            + "to:"
            + receiver_email
            + " after:"
            + str(datetime.date.today()).replace("-", "/")
            if date
            else "subject:" + subject_text + " " + "to:" + receiver_email
        )
        email_html = self.__search_messages(search_string)
        if email_html != None:
            return email_html
        else:
            self.log.warning("Email not found on INBOX. Trying to find it on SPAM ...")
            email_html = self.__search_messages_by_subject_and_receiver_in_spam(
                subject_text, receiver_email, date=True
            )
            return email_html

    def __get_service(self):
        """Connects to the API using Google Cloud credentials.

        Parameters
        ----------
        credentials_path : str, (optional)
            path where you saved your credentials from Google Cloud.

        Returns
        -------
        service
        """

        SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
        try:
            creds = None
            if os.path.exists("token.pickle"):
                with open("token.pickle", "rb") as token:
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    current_directory = pathlib.Path(__file__).parent.parent.resolve()
                    credentials_path = f"{current_directory}\\gmail_credentials.json"
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_path, SCOPES
                    )
                    creds = flow.run_local_server(port=0)
                with open("token.pickle", "wb") as token:
                    pickle.dump(creds, token)
            # Connect to the Gmail API
            service = build("gmail", "v1", credentials=creds)
            return service

        except Exception as e:
            self.log.error("Error getting the service.")
            self.log.error(e)

    def __search_messages(self, search_string, labelId="INBOX", tries=3):
        """Retrieves the id of an email based on a search query
        made with operators. Then retrieves the email with the id.
        Passes the data to get_html_message to obtain the html as string.

        Parameters
        ----------
        search_string : str,
            contains the query operator + element to find
        labelId : str, (optional)
            points the query to a specific email folder, it can be:
            'INBOX', 'SPAM', 'TRASH', 'UNREAD', 'STARRED', 'IMPORTANT', 'SENT', 'DRAFT', 'CATEGORY_PROMOTIONS',
            by default 'INBOX'
        tries: int, (optional)
            shows how many tries the search has to find the email

        Returns
        -------
        email_html : str,
            If found, it returns HTML string of the email, ready to be saved in a document to be used with Selenium, else None.
        """

        try:
            self.log.info(f"Looking for emails on '{labelId}'")
            number_results = 0
            while tries > 0 and number_results == 0:
                search_id = (
                    self.service.users()
                    .messages()
                    .list(
                        userId=self.user_id,
                        maxResults=10,
                        labelIds=[labelId],
                        q=search_string,
                    )
                    .execute()
                )
                number_results = search_id["resultSizeEstimate"]
                tries -= 1
                time.sleep(3)
            if number_results > 0:
                self.log.info("Email found successfully!")
                messages_id = []
                messages = search_id["messages"]
                for message in messages:
                    messages_id.append(message["id"])
                message_id = messages_id[0]
                email_html = self.__get_html(message_id)
                return email_html
            else:
                self.log.info("There where 0 results for that search.")
                return None

        except Exception as e:
            self.log.error("Error searching for the email.")
            self.log.error(e)

    def __get_html(self, message_id):
        """This method receives the email id found by the query, gets the email data, and parse it to html.
        Parameters
        ----------
        message_id : str,
            message id found by the "search_messages" function.

        Returns
        -------
        str,
            HTML of the email if found.
        """

        try:
            message = (
                self.service.users()
                .messages()
                .get(userId=self.user_id, id=message_id)
                .execute()
            )
            payload = message["payload"]
            parts = payload.get("parts")
            for part in parts:
                if part["mimeType"] == "text/html":
                    break
            data = part["body"]["data"]
            data = data.replace("-", "+").replace("_", "/")
            decoded_data = base64.b64decode(data)
            soup = BeautifulSoup(decoded_data, "html.parser")
            soup = str(soup).replace("\n", "").replace("\r", "").replace("\\", "")
            self.log.info("HTML found successfully!")
            return soup
        except Exception as e:
            self.log.error("Error getting the html.")
            self.log.error(e)
