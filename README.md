# crawling_it_news
Python과 Scrapy 활용한 네이버&amp;다음 IT 기사 크롤링

## 📜 프로젝트 개요

이 프로젝트는 네이버와 다음의 IT 뉴스 섹션에서 최신 기사를 자동으로 크롤링하여, 실시간으로 대기질 관련 정보를 모델링하고 분석하는 시스템을 개발하는 것을 목표로 합니다. 이 시스템은 최신 IT 트렌드와 기술 발전에 대한 정보를 신속하게 수집하고 분석하여, 사용자에게 가치 있는 인사이트를 제공하고자 합니다.


이 프로젝트를 사용하기 위한 설치 방법은 다음과 같습니다:

```bash
git clone https://github.com/asthtls/crawling_it_news.git
cd crawling_it_news
pip install -r requirements.txt
```
 

## **🖥 사용 기술**

**언어**: Python

**웹 크롤링 프레임워크**: Scrapy

## **학습 경험 및 도전 과제**

- **Scrapy 파이프라인과 미들웨어**: 이 프로젝트를 통해 Scrapy의 파이프라인과 미들웨어를 깊이 있게 학습했습니다. 특히, 데이터를 처리하고 저장하는 과정에서 파이프라인을 활용하여 크롤링된 데이터의 후처리를 자동화했습니다. 또한, Scrapy 미들웨어를 사용하여 크롤링 과정에서 발생할 수 있는 다양한 문제(예: 요청 차단, IP 밴 등)에 대응하는 방법을 탐구했습니다.
- **동적 웹페이지 크롤링**: JavaScript로 동적으로 생성되는 콘텐츠를 크롤링하는 과정에서 발생한 기술적 도전을 경험하고, Scrapy와 함께 Selenium 등의 도구를 사용하여 이를 해결하는 방법을 배웠습니다

## **프로젝트 성과**

- 네이버와 다음에서 IT 관련 뉴스 기사의 실시간 크롤링 및 데이터베이스 구축을 성공적으로 수행했습니다.
- Scrapy 프레임워크의 고급 기능인 파이프라인과 미들웨어를 활용하여 크롤링 프로세스를 최적화하고, 크롤링 효율성을 크게 향상시켰습니다

## 향후 개선사항

- **웹 사이트 구조적 차이점의 깊이 있는 분석**: 네이버와 다음 웹 사이트 간의 구조적 차이에 대한 보다 깊이 있는 분석을 수행하여, 각 사이트의 HTML 구조와 JavaScript 동작 방식을 더욱 정밀하게 이해할 계획입니다. 이를 통해 크롤링 전략을 더욱 세밀하게 조정하여 데이터 수집의 정확도와 효율성을 향상시킬 수 있습니다.
- **고급 크롤링 기술의 적용**: 동적 콘텐츠의 처리와 웹 사이트별 크롤링 방지 기술에 대응하기 위해, Headless Browser 사용, AJAX 요청 처리 방법 등 고급 크롤링 기술을 적용할 예정입니다. 이를 통해 네이버와 다음의 구조적 차이를 보다 효과적으로 극복하고, 크롤링 범위를 확장할 수 있습니다.
- **사용자 인터페이스 개선**: 사용자가 보다 쉽게 크롤링할 뉴스의 카테고리를 선택하고, 결과를 확인할 수 있는 직관적인 웹 인터페이스를 개발하여 사용자 경험을 향상시킬 계획입니다.
