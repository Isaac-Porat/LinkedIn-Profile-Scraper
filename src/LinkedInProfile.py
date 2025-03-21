from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Union
from datetime import date

@dataclass
class DateInfo:
    day: int
    month: int
    year: int
    
    def to_date(self) -> date:
        return date(self.year, self.month, self.day)

@dataclass
class Project:
    title: str
    description: str
    starts_at: DateInfo
    ends_at: Optional[DateInfo] = None
    url: Optional[str] = None

@dataclass
class Certification:
    authority: str
    name: str
    starts_at: Optional[DateInfo] = None
    ends_at: Optional[DateInfo] = None
    license_number: Optional[str] = None
    url: Optional[str] = None
    display_source: Optional[str] = None

@dataclass
class Education:
    school: str
    degree_name: Optional[str] = None
    field_of_study: Optional[str] = None
    starts_at: Optional[DateInfo] = None
    ends_at: Optional[DateInfo] = None
    description: Optional[str] = None
    school_linkedin_profile_url: Optional[str] = None
    logo_url: Optional[str] = None
    activities_and_societies: Optional[str] = None
    grade: Optional[str] = None
    school_facebook_profile_url: Optional[str] = None

@dataclass
class Experience:
    company: str
    title: str
    description: Optional[str] = None
    starts_at: Optional[DateInfo] = None
    ends_at: Optional[DateInfo] = None
    location: Optional[str] = None
    company_linkedin_profile_url: Optional[str] = None
    logo_url: Optional[str] = None
    company_facebook_profile_url: Optional[str] = None

@dataclass
class Activity:
    title: str
    activity_status: str
    link: str

@dataclass
class Recommendation:
    author: str
    text: str

@dataclass
class SimilarProfile:
    name: str
    link: str
    location: Optional[str] = None
    summary: Optional[str] = None

@dataclass
class LinkedInProfile:
    first_name: str
    last_name: str
    full_name: str
    headline: str
    summary: str
    city: str
    state: str
    country: str
    country_full_name: str
    occupation: str
    connections: int
    profile_pic_url: str
    background_cover_image_url: str
    public_identifier: str
    certifications: List[Certification] = field(default_factory=list)
    education: List[Education] = field(default_factory=list)
    experiences: List[Experience] = field(default_factory=list)
    activities: List[Activity] = field(default_factory=list)
    projects: List[Project] = field(default_factory=list)
    recommendations: List[Recommendation] = field(default_factory=list)
    similarly_named_profiles: List[SimilarProfile] = field(default_factory=list)
    follower_count: Optional[int] = None
    accomplishment_courses: List[Any] = field(default_factory=list)
    accomplishment_honors_awards: List[Any] = field(default_factory=list)
    accomplishment_organisations: List[Any] = field(default_factory=list)
    accomplishment_patents: List[Any] = field(default_factory=list)
    accomplishment_publications: List[Any] = field(default_factory=list)
    accomplishment_test_scores: List[Any] = field(default_factory=list)
    articles: List[Any] = field(default_factory=list)
    groups: List[Any] = field(default_factory=list)
    people_also_viewed: List[Any] = field(default_factory=list)
    volunteer_work: List[Any] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LinkedInProfile":
        """Create a LinkedInProfile instance from a dictionary."""
        # Helper function to convert date dictionaries to DateInfo objects
        def parse_date(date_dict: Optional[Dict[str, int]]) -> Optional[DateInfo]:
            if not date_dict:
                return None
            return DateInfo(
                day=date_dict.get("day", 1),
                month=date_dict.get("month", 1),
                year=date_dict.get("year", 1970)
            )
        
        # Parse projects
        projects = []
        for proj in data.get("accomplishment_projects", []):
            projects.append(Project(
                title=proj.get("title", ""),
                description=proj.get("description", ""),
                starts_at=parse_date(proj.get("starts_at")),
                ends_at=parse_date(proj.get("ends_at")),
                url=proj.get("url")
            ))
        
        # Parse certifications
        certifications = []
        for cert in data.get("certifications", []):
            certifications.append(Certification(
                authority=cert.get("authority", ""),
                name=cert.get("name", ""),
                starts_at=parse_date(cert.get("starts_at")),
                ends_at=parse_date(cert.get("ends_at")),
                license_number=cert.get("license_number"),
                url=cert.get("url"),
                display_source=cert.get("display_source")
            ))
        
        # Parse education
        education = []
        for edu in data.get("education", []):
            education.append(Education(
                school=edu.get("school", ""),
                degree_name=edu.get("degree_name"),
                field_of_study=edu.get("field_of_study"),
                starts_at=parse_date(edu.get("starts_at")),
                ends_at=parse_date(edu.get("ends_at")),
                description=edu.get("description"),
                school_linkedin_profile_url=edu.get("school_linkedin_profile_url"),
                logo_url=edu.get("logo_url"),
                activities_and_societies=edu.get("activities_and_societies"),
                grade=edu.get("grade"),
                school_facebook_profile_url=edu.get("school_facebook_profile_url")
            ))
        
        # Parse experiences
        experiences = []
        for exp in data.get("experiences", []):
            experiences.append(Experience(
                company=exp.get("company", ""),
                title=exp.get("title", ""),
                description=exp.get("description"),
                starts_at=parse_date(exp.get("starts_at")),
                ends_at=parse_date(exp.get("ends_at")),
                location=exp.get("location"),
                company_linkedin_profile_url=exp.get("company_linkedin_profile_url"),
                logo_url=exp.get("logo_url"),
                company_facebook_profile_url=exp.get("company_facebook_profile_url")
            ))
        
        # Parse activities
        activities = []
        for act in data.get("activities", []):
            activities.append(Activity(
                title=act.get("title", ""),
                activity_status=act.get("activity_status", ""),
                link=act.get("link", "")
            ))
        
        # Parse similar profiles
        similar_profiles = []
        for prof in data.get("similarly_named_profiles", []):
            similar_profiles.append(SimilarProfile(
                name=prof.get("name", ""),
                link=prof.get("link", ""),
                location=prof.get("location"),
                summary=prof.get("summary")
            ))
        
        # Create and return the profile
        return cls(
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            full_name=data.get("full_name", ""),
            headline=data.get("headline", ""),
            summary=data.get("summary", ""),
            city=data.get("city", ""),
            state=data.get("state", ""),
            country=data.get("country", ""),
            country_full_name=data.get("country_full_name", ""),
            occupation=data.get("occupation", ""),
            connections=data.get("connections", 0),
            profile_pic_url=data.get("profile_pic_url", ""),
            background_cover_image_url=data.get("background_cover_image_url", ""),
            public_identifier=data.get("public_identifier", ""),
            certifications=certifications,
            education=education,
            experiences=experiences,
            activities=activities,
            projects=projects,
            similarly_named_profiles=similar_profiles,
            follower_count=data.get("follower_count"),
            accomplishment_courses=data.get("accomplishment_courses", []),
            accomplishment_honors_awards=data.get("accomplishment_honors_awards", []),
            accomplishment_organisations=data.get("accomplishment_organisations", []),
            accomplishment_patents=data.get("accomplishment_patents", []),
            accomplishment_publications=data.get("accomplishment_publications", []),
            accomplishment_test_scores=data.get("accomplishment_test_scores", []),
            articles=data.get("articles", []),
            groups=data.get("groups", []),
            people_also_viewed=data.get("people_also_viewed", []),
            volunteer_work=data.get("volunteer_work", [])
        )
