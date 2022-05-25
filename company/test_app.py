from unittest import TestCase
import requests


class JobCreatListView(TestCase):
    def test_company_name_autocomplete(self):
        """
        1. 회사명 자동완성
        회사명의 일부만 들어가도 검색이 되어야 합니다.
        header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
        """
        url = 'http://localhost:8000/api/v1/companies/search/?query=링크'
        headers = {"x-wanted-language": "ko"}
        r = requests.get(url, headers=headers)

        expecting_result = [
            {"company_name": "주식회사 링크드코리아"},
            {"company_name": "스피링크"}
        ]

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), expecting_result)

    def test_company_search(self):
        """
        2. 회사 이름으로 회사 검색
        header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
        """
        url = 'http://localhost:8000/api/v1/companies/Wantedlab/'
        headers = {"x-wanted-language": "ko"}
        r = requests.get(url, headers=headers)

        expecting_result = {
                "company_name": "원티드랩",
                "tags": [
                    "태그_4",
                    "태그_20",
                    "태그_16"
                ]
            }

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), expecting_result)


    def test_new_company(self):
        """
        3.  새로운 회사 추가
        새로운 언어(tw)도 같이 추가 될 수 있습니다.
        저장 완료후 header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
        """
        url = 'http://127.0.0.1:8000/api/v1/companies/'
        headers = {"x-wanted-language": "tw"}
        request_json = {
            "ko":{
                "name":"라인 프레쉬",
                "tags":["태그_1", "태그_8", "태그_15"]
            },
            "tw":{
                "name":"LINE FRESH",
                "tags":["tag_1", "tag_8", "tag_15"]
            },
            "en":{
                "name":"LINE FRESH",
                "tags":["tag_1", "tag_8", "tag_15"]
            }
        }

        expecting_result = {
            "company_name": "LINE FRESH",
            "tags": [
                "tag_1",
                "tag_8",
                "tag_15"
            ]
        }

        r = requests.post(url, headers=headers, json=request_json)

        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), expecting_result)