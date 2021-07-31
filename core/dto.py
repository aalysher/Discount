from .models import Company, Discount, View, Location, SocialMedia


class CompanyDto:
    def __init__(self, company):
        self.name = company.name
        self.description = company.description
        self.photo = company.photo
        self.view = View.objects.get(id=company).counter
        self.percent = Discount.objects.filter(company=company)[0].percent
        self.city = Location.objects.filter(company=company)[0].city


class CompanyListDto:
    def __init__(self, company_queryset):
        self.company_list_dto = [CompanyDto(company) for company in company_queryset]


class DiscountDto(CompanyDto):
    def __init__(self, company):
        super().__init__(company)
        self.social_media = SocialMedia.objects.filter(company=company)
        self.location = Location.objects.get(company=company)
        self.condition = Discount.objects.get(company=company)
        self.instruction = Discount.objects.filter(company=company)[0].instruction.title
