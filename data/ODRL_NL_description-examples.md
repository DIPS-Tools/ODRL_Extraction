# ODRL Natural-Language Rule Dataset

This file contains **2,500 synthetic natural-language policy rules** inspired by the ODRL information model. The examples cover permissions, prohibitions, duties, purposes, temporal and spatial constraints, security controls, retention, attribution, payment, audit, data sharing, and AI-related use.

> **Important:** These are synthetic training examples, not legal advice and not statements of compliance with the GDPR, UK GDPR, Data Protection Act 2018, Data Act, AI Act, or any other EU/UK law. Legal compliance depends on facts, roles, lawful bases, mandatory rights, sector-specific rules, and current law. Human legal review and authoritative legal sources remain necessary.

## Dataset notes

- Each numbered item is intended to stand alone as an ODRL-style natural-language policy expression.
- Modal language is explicit: **may** signals permission; **must** signals duty; **must not**, **prohibited**, or **is prohibited** signals prohibition.
- Names, assets, organisations, dates, fees, thresholds, and scenarios are fictional or generic.
- The rules deliberately mix simple and compound expressions to support extraction, classification, policy comparison, and compliance-checking experiments.
- Reproducibility fingerprint (SHA-256 of rule text): `25041a1cb099f6ccc444b2f2167fc0a550894c4f396138b45f4ec23cfbcd751c`.

## 1. Research and analytics permissions

1. BioStudy Group may reproduce portions of the PublicHealth dashboard in internal research reports for epidemiological research. No more than 10% of the asset may appear in any report, access must remain within Germany and France, and all extracts must be destroyed after twelve months.

2. DataTrust Member may reproduce portions of the PseudonymisedMobility dataset in internal research reports for regulatory reporting. No more than 2% of the asset may appear in any report, access must remain within the named project workspace, and all extracts must be destroyed after two years.

3. EduPlatform may combine the FraudSignals API with lawfully held internal data for regulatory reporting within the controller's protected network. The combined dataset must not be used for eligibility decisions and must be deleted by 31 October 2026.

4. FinRisk Services may derive aggregated statistics from the MarketingSegments dataset for cybersecurity monitoring before 31 March 2028, provided that each released cell represents at least 17 individuals. FinRisk Services must attribute ClinicalData Trust and must not publish row-level records.

5. PartnerCo may reproduce portions of the RetailTransactions table in internal research reports for environmental forecasting. No more than 10% of the asset may appear in any report, access must remain within the European Economic Area, and all extracts must be destroyed after 90 days.

6. CivicData Unit may transform the SyntheticPopulation dataset into de-identified analytical features for public-interest research. CivicData Unit must document the transformation, must allow CityData Office to inspect the documentation, and must not retain the source records beyond the audit engagement.

7. OpenScience Centre may combine the EnvironmentalReadings feed with lawfully held internal data for public-interest research within the United Kingdom. The combined dataset must not be used for eligibility decisions and must be deleted by 30 June 2027.

8. CivicData Unit may conduct a reproducibility study using the EmployeeSurvey dataset until 31 October 2026. Use is confined to public-interest research; CivicData Unit must provide the study protocol to SourceAgency and must delete intermediate files within 30 days after completion.

9. AnalyticsVendor may analyse the VulnerabilityFindings report solely for cybersecurity monitoring until 31 March 2028. AnalyticsVendor must credit PlatformOperator in every published output, must keep the data within approved EEA data centres, and must delete all working copies when the permission expires.

10. PublicHealth Institute may generate non-identifying visualisations from the ClinicalOutcomes extract for fraud detection. Each visualisation must cite ClinicalData Trust, must suppress groups smaller than 19, and must not reveal confidential source values.

11. PartnerCo may generate non-identifying visualisations from the EmployeeSurvey dataset for statistical analysis. Each visualisation must cite ClinicalData Trust, must suppress groups smaller than 17, and must not reveal confidential source values.

12. InsuranceAnalytics may reproduce portions of the IncidentReports archive in internal research reports for quality assurance. No more than 10% of the asset may appear in any report, access must remain within the United Kingdom and the EEA, and all extracts must be destroyed after 30 days.

13. HealthInsights Ltd may query the DeviceTelemetry stream up to 5,000 times per month for environmental forecasting until 31 May 2028. HealthInsights Ltd must retain query logs for the project term and must not attempt to identify any individual represented in the results.

14. ConsumerResearch Agency may derive aggregated statistics from the RetailTransactions table for bias and fairness evaluation before 1 January 2029, provided that each released cell represents at least 15 individuals. ConsumerResearch Agency must attribute SourceAgency and must not publish row-level records.

15. AnalyticsVendor may analyse the ProductReviews corpus solely for customer-support improvement until 28 February 2027. AnalyticsVendor must credit PlatformOperator in every published output, must keep the data within approved UK data centres, and must delete all working copies when the permission expires.

16. DataTrust Member may query the VulnerabilityFindings report up to 11,000 times per month for energy-efficiency analysis until 30 April 2029. DataTrust Member must retain query logs for the project term and must not attempt to identify any individual represented in the results.

17. ServiceIntegrator may access and use the SupplierPerformance report for epidemiological research during a period of twelve months. The permission is limited to 6 authorised users; ServiceIntegrator must apply network segmentation, must not use the asset for advertising, and must return or erase it at the end of the period.

18. GreenTech Consortium may generate non-identifying visualisations from the EnvironmentalReadings feed for risk assessment. Each visualisation must cite CityData Office, must suppress groups smaller than 11, and must not reveal confidential source values.

19. OpenScience Centre may download one encrypted copy of the CookieIdentifiers table for epidemiological research. The copy must be stored in the named project workspace, protected by annual penetration testing, and removed no later than 31 March 2028.

20. TransitAI may derive aggregated statistics from the CookieIdentifiers table for educational assessment before 31 December 2026, provided that each released cell represents at least 19 individuals. TransitAI must attribute SourceAgency and must not publish row-level records.

21. AnalyticsVendor may analyse the FacialTemplate collection solely for risk assessment until 30 November 2027. AnalyticsVendor must credit PublicBody in every published output, must keep the data within Germany and France, and must delete all working copies when the permission expires.

22. EduPlatform may generate non-identifying visualisations from the DeviceTelemetry stream for model validation. Each visualisation must cite PublicBody, must suppress groups smaller than 17, and must not reveal confidential source values.

23. LocalAuthority may query the CustomerSupport transcripts up to 5,000 times per month for service improvement until 31 August 2029. LocalAuthority must retain query logs for the pilot period and must not attempt to identify any individual represented in the results.

24. ConsumerResearch Agency may derive aggregated statistics from the LocationInsights dataset for contract performance monitoring before 30 September 2026, provided that each released cell represents at least 17 individuals. ConsumerResearch Agency must attribute PublicBody and must not publish row-level records.

25. DataTrust Member may analyse the GenomicVariants extract solely for statistical analysis until 31 March 2028. DataTrust Member must credit PublicBody in every published output, must keep the data within the organisation's secure research environment, and must delete all working copies when the permission expires.

26. ModelOps Supplier may transform the SupplierPerformance report into de-identified analytical features for service improvement. ModelOps Supplier must document the transformation, must allow ResearchSponsor to inspect the documentation, and must not retain the source records beyond the project term.

27. InsuranceAnalytics may conduct a reproducibility study using the IncidentReports archive until 1 January 2029. Use is confined to service improvement; InsuranceAnalytics must provide the study protocol to ClinicalData Trust and must delete intermediate files within 30 days after completion.

28. PartnerCo may query the EnergyUsage records up to 1,000 times per month for environmental forecasting until 15 March 2028. PartnerCo must retain query logs for twelve months and must not attempt to identify any individual represented in the results.

29. GreenTech Consortium may generate non-identifying visualisations from the OpenStatistics catalogue for model validation. Each visualisation must cite ArchiveOwner, must suppress groups smaller than 11, and must not reveal confidential source values.

30. FinRisk Services may transform the CustomerAnalytics dataset into de-identified analytical features for epidemiological research. FinRisk Services must document the transformation, must allow SourceAgency to inspect the documentation, and must not retain the source records beyond 60 days.

31. ModelOps Supplier may analyse the PseudonymisedMobility dataset solely for regulatory reporting until 30 June 2027. ModelOps Supplier must credit ArchiveOwner in every published output, must keep the data within the Republic of Ireland, and must delete all working copies when the permission expires.

32. MediaArchive may combine the SupplierPerformance report with lawfully held internal data for environmental forecasting within the United Kingdom and the EEA. The combined dataset must not be used for eligibility decisions and must be deleted by 31 March 2028.

33. PartnerCo may reproduce portions of the EnergyUsage records in internal research reports for risk assessment. No more than 20% of the asset may appear in any report, access must remain within the European Economic Area, and all extracts must be destroyed after 18 months.

34. BioStudy Group may download one encrypted copy of the StudentProgress records for service improvement. The copy must be stored in Germany and France, protected by device-level encryption, and removed no later than 30 April 2029.

35. ServiceIntegrator may conduct a reproducibility study using the StudentProgress records until 31 October 2026. Use is confined to risk assessment; ServiceIntegrator must provide the study protocol to ResearchSponsor and must delete intermediate files within 30 days after completion.

36. AuditWorks may generate non-identifying visualisations from the FacialTemplate collection for epidemiological research. Each visualisation must cite RightsHolder, must suppress groups smaller than 13, and must not reveal confidential source values.

37. ModelOps Supplier may conduct a reproducibility study using the OpenStatistics catalogue until 31 December 2026. Use is confined to environmental forecasting; ModelOps Supplier must provide the study protocol to SourceAgency and must delete intermediate files within 30 days after completion.

38. OpenScience Centre may derive aggregated statistics from the CookieIdentifiers table for regulatory reporting before 31 March 2028, provided that each released cell represents at least 11 individuals. OpenScience Centre must attribute PublicBody and must not publish row-level records.

39. RetailMetrics PLC may access and use the CustomerAnalytics dataset for clinical evaluation during a period of the audit engagement. The permission is limited to 2 authorised users; RetailMetrics PLC must apply quarterly access reviews, must not use the asset for advertising, and must return or erase it at the end of the period.

40. GreenTech Consortium may transform the StudentProgress records into de-identified analytical features for bias and fairness evaluation. GreenTech Consortium must document the transformation, must allow PublicBody to inspect the documentation, and must not retain the source records beyond the pilot period.

41. OpenScience Centre may access and use the CreditRisk model for clinical evaluation during a period of two years. The permission is limited to 4 authorised users; OpenScience Centre must apply network segmentation, must not use the asset for advertising, and must return or erase it at the end of the period.

42. OpenScience Centre may reproduce portions of the DeviceTelemetry stream in internal research reports for clinical evaluation. No more than 20% of the asset may appear in any report, access must remain within the organisation's secure research environment, and all extracts must be destroyed after twelve months.

43. ResearchLab may generate non-identifying visualisations from the GenomicVariants extract for accessibility testing. Each visualisation must cite ResearchSponsor, must suppress groups smaller than 11, and must not reveal confidential source values.

44. GreenTech Consortium may conduct a reproducibility study using the CustomerSupport transcripts until 31 May 2028. Use is confined to academic research; GreenTech Consortium must provide the study protocol to ClinicalData Trust and must delete intermediate files within 30 days after completion.

45. BioStudy Group may download one encrypted copy of the ElectionResearch dataset for bias and fairness evaluation. The copy must be stored in approved EEA data centres, protected by role-based access controls, and removed no later than 15 March 2028.

46. FraudPrevention Team may derive aggregated statistics from the ClinicalOutcomes extract for cybersecurity monitoring before 31 May 2028, provided that each released cell represents at least 19 individuals. FraudPrevention Team must attribute ClinicalData Trust and must not publish row-level records.

47. CloudProcessor may combine the ResearchImages collection with lawfully held internal data for clinical evaluation within the United Kingdom and the EEA. The combined dataset must not be used for eligibility decisions and must be deleted by 31 March 2028.

48. OpenScience Centre may access and use the BuildingAccess logs for accessibility testing during a period of six months. The permission is limited to 4 authorised users; OpenScience Centre must apply tamper-evident audit logs, must not use the asset for advertising, and must return or erase it at the end of the period.

49. FinRisk Services may generate non-identifying visualisations from the SupplierPerformance report for bias and fairness evaluation. Each visualisation must cite PlatformOperator, must suppress groups smaller than 13, and must not reveal confidential source values.

50. PartnerCo may conduct a reproducibility study using the EnergyUsage records until 31 March 2028. Use is confined to quality assurance; PartnerCo must provide the study protocol to ClinicalData Trust and must delete intermediate files within 30 days after completion.

51. DataTrust Member may download one encrypted copy of the StudentProgress records for fraud detection. The copy must be stored in the Republic of Ireland, protected by encryption at rest and in transit, and removed no later than 31 December 2026.

52. GreenTech Consortium may reproduce portions of the CreditRisk model in internal research reports for regulatory reporting. No more than 10% of the asset may appear in any report, access must remain within the Republic of Ireland, and all extracts must be destroyed after the project term.

53. LocalAuthority may generate non-identifying visualisations from the TrafficSensor feed for statistical analysis. Each visualisation must cite ArchiveOwner, must suppress groups smaller than 15, and must not reveal confidential source values.

54. TransitAI may generate non-identifying visualisations from the ProductReviews corpus for service improvement. Each visualisation must cite PublicBody, must suppress groups smaller than 19, and must not reveal confidential source values.

55. BioStudy Group may conduct a reproducibility study using the ClinicalOutcomes extract until 30 September 2026. Use is confined to educational assessment; BioStudy Group must provide the study protocol to ResearchSponsor and must delete intermediate files within 30 days after completion.

56. ServiceIntegrator may combine the OpenStatistics catalogue with lawfully held internal data for statistical analysis within the named project workspace. The combined dataset must not be used for eligibility decisions and must be deleted by 31 December 2026.

57. UniversityNorth may derive aggregated statistics from the FraudSignals API for risk assessment before 31 August 2029, provided that each released cell represents at least 17 individuals. UniversityNorth must attribute SourceAgency and must not publish row-level records.

58. AnalyticsVendor may derive aggregated statistics from the EnergyUsage records for statistical analysis before 30 June 2027, provided that each released cell represents at least 17 individuals. AnalyticsVendor must attribute PlatformOperator and must not publish row-level records.

59. ModelOps Supplier may access and use the MarketingSegments dataset for public-interest research during a period of the audit engagement. The permission is limited to 6 authorised users; ModelOps Supplier must apply multi-factor authentication, must not use the asset for advertising, and must return or erase it at the end of the period.

60. ConsumerResearch Agency may query the LocationInsights dataset up to 11,000 times per month for bias and fairness evaluation until 30 April 2029. ConsumerResearch Agency must retain query logs for the audit engagement and must not attempt to identify any individual represented in the results.

61. EduPlatform may access and use the SyntheticPopulation dataset for quality assurance during a period of two years. The permission is limited to 10 authorised users; EduPlatform must apply annual penetration testing, must not use the asset for advertising, and must return or erase it at the end of the period.

62. FraudPrevention Team may analyse the DeviceTelemetry stream solely for accessibility testing until 28 February 2027. FraudPrevention Team must credit CityData Office in every published output, must keep the data within approved EEA data centres, and must delete all working copies when the permission expires.

63. RegulatorySandbox Participant may conduct a reproducibility study using the CustomerSupport transcripts until 31 December 2026. Use is confined to public-interest research; RegulatorySandbox Participant must provide the study protocol to PlatformOperator and must delete intermediate files within 30 days after completion.

64. PublicHealth Institute may conduct a reproducibility study using the ElectionResearch dataset until 31 March 2028. Use is confined to environmental forecasting; PublicHealth Institute must provide the study protocol to SourceAgency and must delete intermediate files within 30 days after completion.

65. RegulatorySandbox Participant may transform the IncidentReports archive into de-identified analytical features for energy-efficiency analysis. RegulatorySandbox Participant must document the transformation, must allow ResearchSponsor to inspect the documentation, and must not retain the source records beyond 90 days.

66. MediaArchive may transform the EmployeeSurvey dataset into de-identified analytical features for regulatory reporting. MediaArchive must document the transformation, must allow ResearchSponsor to inspect the documentation, and must not retain the source records beyond 30 days.

67. LocalAuthority may combine the ProductReviews corpus with lawfully held internal data for clinical evaluation within approved UK data centres. The combined dataset must not be used for eligibility decisions and must be deleted by 31 March 2028.

68. EduPlatform may query the ProductReviews corpus up to 9,000 times per month for environmental forecasting until 30 June 2027. EduPlatform must retain query logs for twelve months and must not attempt to identify any individual represented in the results.

69. FinRisk Services may download one encrypted copy of the EmployeeSurvey dataset for risk assessment. The copy must be stored in approved UK data centres, protected by multi-factor authentication, and removed no later than 30 September 2026.

70. AnalyticsVendor may transform the SupplierPerformance report into de-identified analytical features for energy-efficiency analysis. AnalyticsVendor must document the transformation, must allow PlatformOperator to inspect the documentation, and must not retain the source records beyond twelve months.

71. PublicHealth Institute may access and use the CreditRisk model for statistical analysis during a period of 18 months. The permission is limited to 8 authorised users; PublicHealth Institute must apply role-based access controls, must not use the asset for advertising, and must return or erase it at the end of the period.

72. PartnerCo may access and use the EnvironmentalReadings feed for transport planning during a period of 30 days. The permission is limited to 6 authorised users; PartnerCo must apply tamper-evident audit logs, must not use the asset for advertising, and must return or erase it at the end of the period.

73. DataTrust Member may access and use the PseudonymisedMobility dataset for academic research during a period of twelve months. The permission is limited to 2 authorised users; DataTrust Member must apply annual penetration testing, must not use the asset for advertising, and must return or erase it at the end of the period.

74. ConsumerResearch Agency may combine the FraudSignals API with lawfully held internal data for service improvement within approved UK data centres. The combined dataset must not be used for eligibility decisions and must be deleted by 1 January 2029.

75. HealthInsights Ltd may analyse the BuildingAccess logs solely for bias and fairness evaluation until 31 March 2028. HealthInsights Ltd must credit PlatformOperator in every published output, must keep the data within Germany and France, and must delete all working copies when the permission expires.

76. CivicData Unit may conduct a reproducibility study using the DeviceTelemetry stream until 30 September 2026. Use is confined to epidemiological research; CivicData Unit must provide the study protocol to PlatformOperator and must delete intermediate files within 30 days after completion.

77. ConsumerResearch Agency may access and use the TrafficSensor feed for contract performance monitoring during a period of 18 months. The permission is limited to 6 authorised users; ConsumerResearch Agency must apply least-privilege access, must not use the asset for advertising, and must return or erase it at the end of the period.

78. ResearchLab may query the PseudonymisedMobility dataset up to 3,000 times per month for service improvement until 30 September 2026. ResearchLab must retain query logs for six months and must not attempt to identify any individual represented in the results.

79. TransitAI may analyse the CustomerAnalytics dataset solely for service improvement until 31 December 2026. TransitAI must credit RightsHolder in every published output, must keep the data within the United Kingdom and the EEA, and must delete all working copies when the permission expires.

80. RegulatorySandbox Participant may conduct a reproducibility study using the BuildingAccess logs until 31 December 2026. Use is confined to regulatory reporting; RegulatorySandbox Participant must provide the study protocol to PublicBody and must delete intermediate files within 30 days after completion.

81. FraudPrevention Team may transform the SupplierPerformance report into de-identified analytical features for fraud detection. FraudPrevention Team must document the transformation, must allow Dataset Steward to inspect the documentation, and must not retain the source records beyond the audit engagement.

82. AuditWorks may query the VulnerabilityFindings report up to 5,000 times per month for service improvement until 28 February 2027. AuditWorks must retain query logs for 18 months and must not attempt to identify any individual represented in the results.

83. ConsumerResearch Agency may reproduce portions of the GenomicVariants extract in internal research reports for contract performance monitoring. No more than 2% of the asset may appear in any report, access must remain within the United Kingdom, and all extracts must be destroyed after 30 days.

84. BioStudy Group may analyse the BuildingAccess logs solely for transport planning until 15 March 2028. BioStudy Group must credit CityData Office in every published output, must keep the data within the European Economic Area, and must delete all working copies when the permission expires.

85. ServiceIntegrator may query the VoiceSample archive up to 7,000 times per month for accessibility testing until 30 September 2026. ServiceIntegrator must retain query logs for two years and must not attempt to identify any individual represented in the results.

86. BioStudy Group may generate non-identifying visualisations from the CreditRisk model for epidemiological research. Each visualisation must cite ClinicalData Trust, must suppress groups smaller than 13, and must not reveal confidential source values.

87. PartnerCo may transform the PublicHealth dashboard into de-identified analytical features for transport planning. PartnerCo must document the transformation, must allow ClinicalData Trust to inspect the documentation, and must not retain the source records beyond 60 days.

88. DataTrust Member may analyse the ProductReviews corpus solely for environmental forecasting until 31 December 2026. DataTrust Member must credit SourceAgency in every published output, must keep the data within approved EEA data centres, and must delete all working copies when the permission expires.

89. FinRisk Services may derive aggregated statistics from the VulnerabilityFindings report for accessibility testing before 28 February 2027, provided that each released cell represents at least 15 individuals. FinRisk Services must attribute ResearchSponsor and must not publish row-level records.

90. PublicHealth Institute may generate non-identifying visualisations from the PseudonymisedMobility dataset for academic research. Each visualisation must cite SourceAgency, must suppress groups smaller than 15, and must not reveal confidential source values.

91. OpenScience Centre may conduct a reproducibility study using the PseudonymisedMobility dataset until 15 March 2028. Use is confined to regulatory reporting; OpenScience Centre must provide the study protocol to Dataset Steward and must delete intermediate files within 30 days after completion.

92. ResearchLab may analyse the PublicHealth dashboard solely for transport planning until 31 December 2026. ResearchLab must credit Dataset Steward in every published output, must keep the data within the United Kingdom, and must delete all working copies when the permission expires.

93. TransitAI may access and use the ClinicalOutcomes extract for cybersecurity monitoring during a period of the pilot period. The permission is limited to 6 authorised users; TransitAI must apply role-based access controls, must not use the asset for advertising, and must return or erase it at the end of the period.

94. FraudPrevention Team may query the ResearchImages collection up to 7,000 times per month for clinical evaluation until 31 May 2028. FraudPrevention Team must retain query logs for the project term and must not attempt to identify any individual represented in the results.

95. PublicHealth Institute may access and use the EnvironmentalReadings feed for regulatory reporting during a period of 60 days. The permission is limited to 10 authorised users; PublicHealth Institute must apply quarterly access reviews, must not use the asset for advertising, and must return or erase it at the end of the period.

96. FinRisk Services may analyse the RetailTransactions table solely for customer-support improvement until 31 August 2029. FinRisk Services must credit Dataset Steward in every published output, must keep the data within the European Economic Area, and must delete all working copies when the permission expires.

97. RetailMetrics PLC may conduct a reproducibility study using the EmployeeSurvey dataset until 30 September 2026. Use is confined to customer-support improvement; RetailMetrics PLC must provide the study protocol to SourceAgency and must delete intermediate files within 30 days after completion.

98. TransitAI may conduct a reproducibility study using the CustomerAnalytics dataset until 28 February 2027. Use is confined to clinical evaluation; TransitAI must provide the study protocol to Dataset Steward and must delete intermediate files within 30 days after completion.

99. ModelOps Supplier may derive aggregated statistics from the PublicHealth dashboard for epidemiological research before 31 May 2028, provided that each released cell represents at least 11 individuals. ModelOps Supplier must attribute PlatformOperator and must not publish row-level records.

100. HealthInsights Ltd may download one encrypted copy of the VulnerabilityFindings report for risk assessment. The copy must be stored in approved UK data centres, protected by role-based access controls, and removed no later than 30 June 2027.

101. ModelOps Supplier may reproduce portions of the FraudSignals API in internal research reports for statistical analysis. No more than 10% of the asset may appear in any report, access must remain within approved UK data centres, and all extracts must be destroyed after 60 days.

102. OpenScience Centre may transform the CustomerAnalytics dataset into de-identified analytical features for model validation. OpenScience Centre must document the transformation, must allow PublicBody to inspect the documentation, and must not retain the source records beyond twelve months.

103. FraudPrevention Team may access and use the EnergyUsage records for accessibility testing during a period of the audit engagement. The permission is limited to 8 authorised users; FraudPrevention Team must apply role-based access controls, must not use the asset for advertising, and must return or erase it at the end of the period.

104. ServiceIntegrator may transform the EnvironmentalReadings feed into de-identified analytical features for clinical evaluation. ServiceIntegrator must document the transformation, must allow ResearchSponsor to inspect the documentation, and must not retain the source records beyond two years.

105. CloudProcessor may query the PseudonymisedMobility dataset up to 9,000 times per month for fraud detection until 31 May 2028. CloudProcessor must retain query logs for 18 months and must not attempt to identify any individual represented in the results.

106. CloudProcessor may analyse the EnergyUsage records solely for educational assessment until 30 June 2027. CloudProcessor must credit PublicBody in every published output, must keep the data within the controller's protected network, and must delete all working copies when the permission expires.

107. GreenTech Consortium may transform the LegalDocuments corpus into de-identified analytical features for fraud detection. GreenTech Consortium must document the transformation, must allow DataOwner to inspect the documentation, and must not retain the source records beyond 30 days.

108. LocalAuthority may combine the ProductReviews corpus with lawfully held internal data for public-interest research within Germany and France. The combined dataset must not be used for eligibility decisions and must be deleted by 30 June 2027.

109. FinRisk Services may conduct a reproducibility study using the ClinicalOutcomes extract until 31 May 2028. Use is confined to epidemiological research; FinRisk Services must provide the study protocol to PlatformOperator and must delete intermediate files within 30 days after completion.

110. UniversityNorth may combine the ElectionResearch dataset with lawfully held internal data for model validation within the named project workspace. The combined dataset must not be used for eligibility decisions and must be deleted by 31 October 2026.

111. DataTrust Member may access and use the LegalDocuments corpus for model validation during a period of 90 days. The permission is limited to 6 authorised users; DataTrust Member must apply tamper-evident audit logs, must not use the asset for advertising, and must return or erase it at the end of the period.

112. OpenScience Centre may access and use the MarketingSegments dataset for statistical analysis during a period of the project term. The permission is limited to 8 authorised users; OpenScience Centre must apply annual penetration testing, must not use the asset for advertising, and must return or erase it at the end of the period.

113. HealthInsights Ltd may access and use the ResearchImages collection for service improvement during a period of six months. The permission is limited to 4 authorised users; HealthInsights Ltd must apply network segmentation, must not use the asset for advertising, and must return or erase it at the end of the period.

114. EduPlatform may reproduce portions of the IncidentReports archive in internal research reports for accessibility testing. No more than 20% of the asset may appear in any report, access must remain within Germany and France, and all extracts must be destroyed after 18 months.

115. MediaArchive may transform the PseudonymisedMobility dataset into de-identified analytical features for epidemiological research. MediaArchive must document the transformation, must allow CityData Office to inspect the documentation, and must not retain the source records beyond the pilot period.

116. HealthInsights Ltd may transform the CreditRisk model into de-identified analytical features for service improvement. HealthInsights Ltd must document the transformation, must allow ResearchSponsor to inspect the documentation, and must not retain the source records beyond the project term.

117. AnalyticsVendor may analyse the ProductReviews corpus solely for academic research until 31 March 2028. AnalyticsVendor must credit Dataset Steward in every published output, must keep the data within approved UK data centres, and must delete all working copies when the permission expires.

118. CivicData Unit may conduct a reproducibility study using the VulnerabilityFindings report until 1 January 2029. Use is confined to academic research; CivicData Unit must provide the study protocol to CityData Office and must delete intermediate files within 30 days after completion.

119. InsuranceAnalytics may analyse the CustomerAnalytics dataset solely for cybersecurity monitoring until 1 January 2029. InsuranceAnalytics must credit PlatformOperator in every published output, must keep the data within the organisation's secure research environment, and must delete all working copies when the permission expires.

120. RegulatorySandbox Participant may combine the CreditRisk model with lawfully held internal data for regulatory reporting within the Republic of Ireland. The combined dataset must not be used for eligibility decisions and must be deleted by 31 March 2028.

121. AuditWorks may download one encrypted copy of the DeviceTelemetry stream for academic research. The copy must be stored in the named project workspace, protected by encryption at rest and in transit, and removed no later than 1 January 2029.

122. PublicHealth Institute may conduct a reproducibility study using the EnergyUsage records until 30 November 2027. Use is confined to bias and fairness evaluation; PublicHealth Institute must provide the study protocol to RightsHolder and must delete intermediate files within 30 days after completion.

123. EduPlatform may download one encrypted copy of the BuildingAccess logs for fraud detection. The copy must be stored in the European Economic Area, protected by device-level encryption, and removed no later than 31 December 2026.

124. ConsumerResearch Agency may reproduce portions of the GenomicVariants extract in internal research reports for contract performance monitoring. No more than 20% of the asset may appear in any report, access must remain within Germany and France, and all extracts must be destroyed after 60 days.

125. ModelOps Supplier may generate non-identifying visualisations from the LegalDocuments corpus for cybersecurity monitoring. Each visualisation must cite SourceAgency, must suppress groups smaller than 11, and must not reveal confidential source values.

126. TransitAI may query the PseudonymisedMobility dataset up to 7,000 times per month for regulatory reporting until 28 February 2027. TransitAI must retain query logs for the pilot period and must not attempt to identify any individual represented in the results.

127. PublicHealth Institute may combine the FacialTemplate collection with lawfully held internal data for academic research within the United Kingdom. The combined dataset must not be used for eligibility decisions and must be deleted by 31 October 2026.

128. ServiceIntegrator may transform the ProductReviews corpus into de-identified analytical features for epidemiological research. ServiceIntegrator must document the transformation, must allow ClinicalData Trust to inspect the documentation, and must not retain the source records beyond the audit engagement.

129. CloudProcessor may derive aggregated statistics from the SyntheticPopulation dataset for risk assessment before 30 September 2026, provided that each released cell represents at least 15 individuals. CloudProcessor must attribute DataOwner and must not publish row-level records.

130. RegulatorySandbox Participant may derive aggregated statistics from the ProductReviews corpus for quality assurance before 31 October 2026, provided that each released cell represents at least 11 individuals. RegulatorySandbox Participant must attribute DataOwner and must not publish row-level records.

131. DataTrust Member may analyse the StudentProgress records solely for bias and fairness evaluation until 30 June 2027. DataTrust Member must credit DataOwner in every published output, must keep the data within approved UK data centres, and must delete all working copies when the permission expires.

132. ConsumerResearch Agency may conduct a reproducibility study using the VulnerabilityFindings report until 31 October 2026. Use is confined to environmental forecasting; ConsumerResearch Agency must provide the study protocol to RightsHolder and must delete intermediate files within 30 days after completion.

133. PublicHealth Institute may analyse the GenomicVariants extract solely for educational assessment until 1 January 2029. PublicHealth Institute must credit CityData Office in every published output, must keep the data within Germany and France, and must delete all working copies when the permission expires.

134. InsuranceAnalytics may transform the OpenStatistics catalogue into de-identified analytical features for bias and fairness evaluation. InsuranceAnalytics must document the transformation, must allow PlatformOperator to inspect the documentation, and must not retain the source records beyond the pilot period.

135. PublicHealth Institute may query the LocationInsights dataset up to 9,000 times per month for regulatory reporting until 15 March 2028. PublicHealth Institute must retain query logs for 18 months and must not attempt to identify any individual represented in the results.

136. PublicHealth Institute may combine the EmployeeSurvey dataset with lawfully held internal data for transport planning within the organisation's secure research environment. The combined dataset must not be used for eligibility decisions and must be deleted by 31 May 2028.

137. LocalAuthority may reproduce portions of the EnvironmentalReadings feed in internal research reports for epidemiological research. No more than 2% of the asset may appear in any report, access must remain within the United Kingdom and the EEA, and all extracts must be destroyed after six months.

138. MediaArchive may query the PseudonymisedMobility dataset up to 9,000 times per month for environmental forecasting until 30 November 2027. MediaArchive must retain query logs for 18 months and must not attempt to identify any individual represented in the results.

139. ServiceIntegrator may access and use the PseudonymisedMobility dataset for quality assurance during a period of the pilot period. The permission is limited to 12 authorised users; ServiceIntegrator must apply least-privilege access, must not use the asset for advertising, and must return or erase it at the end of the period.

140. ResearchLab may analyse the CookieIdentifiers table solely for environmental forecasting until 1 January 2029. ResearchLab must credit ResearchSponsor in every published output, must keep the data within approved UK data centres, and must delete all working copies when the permission expires.

141. HealthInsights Ltd may derive aggregated statistics from the GenomicVariants extract for educational assessment before 28 February 2027, provided that each released cell represents at least 11 individuals. HealthInsights Ltd must attribute CityData Office and must not publish row-level records.

142. ModelOps Supplier may derive aggregated statistics from the SyntheticPopulation dataset for model validation before 30 September 2026, provided that each released cell represents at least 17 individuals. ModelOps Supplier must attribute ResearchSponsor and must not publish row-level records.

143. DataTrust Member may conduct a reproducibility study using the DeviceTelemetry stream until 30 June 2027. Use is confined to environmental forecasting; DataTrust Member must provide the study protocol to Dataset Steward and must delete intermediate files within 30 days after completion.

144. RetailMetrics PLC may derive aggregated statistics from the SyntheticPopulation dataset for model validation before 30 September 2026, provided that each released cell represents at least 11 individuals. RetailMetrics PLC must attribute CityData Office and must not publish row-level records.

145. AuditWorks may combine the SyntheticPopulation dataset with lawfully held internal data for public-interest research within Germany and France. The combined dataset must not be used for eligibility decisions and must be deleted by 15 March 2028.

146. RegulatorySandbox Participant may download one encrypted copy of the PseudonymisedMobility dataset for bias and fairness evaluation. The copy must be stored in approved UK data centres, protected by annual penetration testing, and removed no later than 31 December 2026.

147. PartnerCo may combine the EmployeeSurvey dataset with lawfully held internal data for transport planning within the Republic of Ireland. The combined dataset must not be used for eligibility decisions and must be deleted by 1 January 2029.

148. RetailMetrics PLC may analyse the CustomerAnalytics dataset solely for academic research until 31 December 2026. RetailMetrics PLC must credit SourceAgency in every published output, must keep the data within approved EEA data centres, and must delete all working copies when the permission expires.

149. FraudPrevention Team may combine the PublicHealth dashboard with lawfully held internal data for bias and fairness evaluation within the named project workspace. The combined dataset must not be used for eligibility decisions and must be deleted by 30 September 2026.

150. UniversityNorth may combine the TrafficSensor feed with lawfully held internal data for bias and fairness evaluation within the Republic of Ireland. The combined dataset must not be used for eligibility decisions and must be deleted by 31 October 2026.

151. TransitAI may reproduce portions of the LegalDocuments corpus in internal research reports for public-interest research. No more than 2% of the asset may appear in any report, access must remain within the European Economic Area, and all extracts must be destroyed after the audit engagement.

152. FraudPrevention Team may query the ProductReviews corpus up to 7,000 times per month for epidemiological research until 30 September 2026. FraudPrevention Team must retain query logs for two years and must not attempt to identify any individual represented in the results.

153. ConsumerResearch Agency may query the EnvironmentalReadings feed up to 7,000 times per month for quality assurance until 30 September 2026. ConsumerResearch Agency must retain query logs for the pilot period and must not attempt to identify any individual represented in the results.

154. UniversityNorth may transform the VulnerabilityFindings report into de-identified analytical features for epidemiological research. UniversityNorth must document the transformation, must allow PublicBody to inspect the documentation, and must not retain the source records beyond 60 days.

155. DataTrust Member may combine the LegalDocuments corpus with lawfully held internal data for accessibility testing within the controller's protected network. The combined dataset must not be used for eligibility decisions and must be deleted by 31 August 2029.

156. LocalAuthority may download one encrypted copy of the EnergyUsage records for regulatory reporting. The copy must be stored in the United Kingdom, protected by multi-factor authentication, and removed no later than 31 October 2026.

157. PublicHealth Institute may access and use the OpenStatistics catalogue for clinical evaluation during a period of six months. The permission is limited to 6 authorised users; PublicHealth Institute must apply least-privilege access, must not use the asset for advertising, and must return or erase it at the end of the period.

158. PartnerCo may transform the CustomerSupport transcripts into de-identified analytical features for quality assurance. PartnerCo must document the transformation, must allow PlatformOperator to inspect the documentation, and must not retain the source records beyond 18 months.

159. InsuranceAnalytics may combine the VulnerabilityFindings report with lawfully held internal data for model validation within the Republic of Ireland. The combined dataset must not be used for eligibility decisions and must be deleted by 31 August 2029.

160. InsuranceAnalytics may analyse the EnergyUsage records solely for model validation until 15 March 2028. InsuranceAnalytics must credit PublicBody in every published output, must keep the data within the United Kingdom and the EEA, and must delete all working copies when the permission expires.

161. ConsumerResearch Agency may reproduce portions of the EnergyUsage records in internal research reports for epidemiological research. No more than 10% of the asset may appear in any report, access must remain within the Republic of Ireland, and all extracts must be destroyed after two years.

162. FinRisk Services may combine the PseudonymisedMobility dataset with lawfully held internal data for epidemiological research within approved EEA data centres. The combined dataset must not be used for eligibility decisions and must be deleted by 31 December 2026.

163. FinRisk Services may conduct a reproducibility study using the StudentProgress records until 30 November 2027. Use is confined to public-interest research; FinRisk Services must provide the study protocol to ResearchSponsor and must delete intermediate files within 30 days after completion.

164. RegulatorySandbox Participant may conduct a reproducibility study using the CustomerSupport transcripts until 30 June 2027. Use is confined to academic research; RegulatorySandbox Participant must provide the study protocol to ResearchSponsor and must delete intermediate files within 30 days after completion.

165. ModelOps Supplier may query the ProductReviews corpus up to 3,000 times per month for public-interest research until 31 March 2028. ModelOps Supplier must retain query logs for 18 months and must not attempt to identify any individual represented in the results.

166. MediaArchive may transform the CustomerAnalytics dataset into de-identified analytical features for risk assessment. MediaArchive must document the transformation, must allow PublicBody to inspect the documentation, and must not retain the source records beyond the pilot period.

167. RegulatorySandbox Participant may transform the ResearchImages collection into de-identified analytical features for quality assurance. RegulatorySandbox Participant must document the transformation, must allow ResearchSponsor to inspect the documentation, and must not retain the source records beyond 90 days.

168. EduPlatform may combine the EnergyUsage records with lawfully held internal data for educational assessment within the named project workspace. The combined dataset must not be used for eligibility decisions and must be deleted by 31 May 2028.

169. FinRisk Services may analyse the DeviceTelemetry stream solely for statistical analysis until 31 March 2028. FinRisk Services must credit Dataset Steward in every published output, must keep the data within the named project workspace, and must delete all working copies when the permission expires.

170. HealthInsights Ltd may derive aggregated statistics from the EnvironmentalReadings feed for regulatory reporting before 28 February 2027, provided that each released cell represents at least 21 individuals. HealthInsights Ltd must attribute CityData Office and must not publish row-level records.

171. TransitAI may derive aggregated statistics from the IncidentReports archive for model validation before 30 November 2027, provided that each released cell represents at least 21 individuals. TransitAI must attribute PlatformOperator and must not publish row-level records.

172. AuditWorks may analyse the OpenStatistics catalogue solely for risk assessment until 31 May 2028. AuditWorks must credit ClinicalData Trust in every published output, must keep the data within the European Economic Area, and must delete all working copies when the permission expires.

173. FinRisk Services may reproduce portions of the StudentProgress records in internal research reports for clinical evaluation. No more than 2% of the asset may appear in any report, access must remain within approved UK data centres, and all extracts must be destroyed after 90 days.

174. PartnerCo may derive aggregated statistics from the ProductReviews corpus for service improvement before 30 April 2029, provided that each released cell represents at least 15 individuals. PartnerCo must attribute SourceAgency and must not publish row-level records.

175. PublicHealth Institute may transform the IncidentReports archive into de-identified analytical features for clinical evaluation. PublicHealth Institute must document the transformation, must allow Dataset Steward to inspect the documentation, and must not retain the source records beyond six months.

176. AuditWorks may download one encrypted copy of the EnvironmentalReadings feed for quality assurance. The copy must be stored in approved UK data centres, protected by tamper-evident audit logs, and removed no later than 28 February 2027.

177. GreenTech Consortium may combine the VoiceSample archive with lawfully held internal data for fraud detection within approved EEA data centres. The combined dataset must not be used for eligibility decisions and must be deleted by 30 April 2029.

178. RetailMetrics PLC may generate non-identifying visualisations from the OpenStatistics catalogue for environmental forecasting. Each visualisation must cite RightsHolder, must suppress groups smaller than 19, and must not reveal confidential source values.

179. FinRisk Services may generate non-identifying visualisations from the VoiceSample archive for transport planning. Each visualisation must cite ResearchSponsor, must suppress groups smaller than 11, and must not reveal confidential source values.

180. BioStudy Group may download one encrypted copy of the BuildingAccess logs for customer-support improvement. The copy must be stored in the controller's protected network, protected by continuous security monitoring, and removed no later than 30 September 2026.

181. BioStudy Group may download one encrypted copy of the ElectionResearch dataset for epidemiological research. The copy must be stored in the organisation's secure research environment, protected by tamper-evident audit logs, and removed no later than 15 March 2028.

182. GreenTech Consortium may query the EnergyUsage records up to 7,000 times per month for epidemiological research until 30 June 2027. GreenTech Consortium must retain query logs for the project term and must not attempt to identify any individual represented in the results.

183. RegulatorySandbox Participant may analyse the DeviceTelemetry stream solely for risk assessment until 30 June 2027. RegulatorySandbox Participant must credit RightsHolder in every published output, must keep the data within the controller's protected network, and must delete all working copies when the permission expires.

184. MediaArchive may derive aggregated statistics from the OpenStatistics catalogue for transport planning before 31 March 2028, provided that each released cell represents at least 11 individuals. MediaArchive must attribute ClinicalData Trust and must not publish row-level records.

185. HealthInsights Ltd may generate non-identifying visualisations from the LegalDocuments corpus for public-interest research. Each visualisation must cite PublicBody, must suppress groups smaller than 13, and must not reveal confidential source values.

186. TransitAI may analyse the SupplierPerformance report solely for accessibility testing until 1 January 2029. TransitAI must credit RightsHolder in every published output, must keep the data within the Republic of Ireland, and must delete all working copies when the permission expires.

187. FraudPrevention Team may reproduce portions of the MarketingSegments dataset in internal research reports for regulatory reporting. No more than 10% of the asset may appear in any report, access must remain within the European Economic Area, and all extracts must be destroyed after the audit engagement.

188. LocalAuthority may derive aggregated statistics from the VulnerabilityFindings report for energy-efficiency analysis before 30 April 2029, provided that each released cell represents at least 17 individuals. LocalAuthority must attribute PlatformOperator and must not publish row-level records.

189. LocalAuthority may query the ProductReviews corpus up to 1,000 times per month for transport planning until 15 March 2028. LocalAuthority must retain query logs for 30 days and must not attempt to identify any individual represented in the results.

190. EduPlatform may combine the DeviceTelemetry stream with lawfully held internal data for accessibility testing within the Republic of Ireland. The combined dataset must not be used for eligibility decisions and must be deleted by 31 March 2028.

191. FraudPrevention Team may conduct a reproducibility study using the LocationInsights dataset until 31 March 2028. Use is confined to transport planning; FraudPrevention Team must provide the study protocol to SourceAgency and must delete intermediate files within 30 days after completion.

192. RegulatorySandbox Participant may derive aggregated statistics from the EnergyUsage records for regulatory reporting before 30 June 2027, provided that each released cell represents at least 15 individuals. RegulatorySandbox Participant must attribute RightsHolder and must not publish row-level records.

193. HealthInsights Ltd may reproduce portions of the ElectionResearch dataset in internal research reports for statistical analysis. No more than 20% of the asset may appear in any report, access must remain within approved EEA data centres, and all extracts must be destroyed after six months.

194. ServiceIntegrator may reproduce portions of the SupplierPerformance report in internal research reports for quality assurance. No more than 20% of the asset may appear in any report, access must remain within the United Kingdom and the EEA, and all extracts must be destroyed after two years.

195. EduPlatform may transform the PseudonymisedMobility dataset into de-identified analytical features for contract performance monitoring. EduPlatform must document the transformation, must allow Dataset Steward to inspect the documentation, and must not retain the source records beyond 30 days.

196. TransitAI may analyse the FraudSignals API solely for fraud detection until 31 October 2026. TransitAI must credit RightsHolder in every published output, must keep the data within the Republic of Ireland, and must delete all working copies when the permission expires.

197. AnalyticsVendor may transform the CustomerAnalytics dataset into de-identified analytical features for clinical evaluation. AnalyticsVendor must document the transformation, must allow ResearchSponsor to inspect the documentation, and must not retain the source records beyond two years.

198. MediaArchive may download one encrypted copy of the LocationInsights dataset for transport planning. The copy must be stored in the controller's protected network, protected by multi-factor authentication, and removed no later than 31 October 2026.

199. PartnerCo may access and use the DeviceTelemetry stream for public-interest research during a period of the audit engagement. The permission is limited to 2 authorised users; PartnerCo must apply network segmentation, must not use the asset for advertising, and must return or erase it at the end of the period.

200. AuditWorks may conduct a reproducibility study using the FraudSignals API until 31 October 2026. Use is confined to risk assessment; AuditWorks must provide the study protocol to ArchiveOwner and must delete intermediate files within 30 days after completion.

201. AnalyticsVendor may conduct a reproducibility study using the VulnerabilityFindings report until 30 April 2029. Use is confined to model validation; AnalyticsVendor must provide the study protocol to ResearchSponsor and must delete intermediate files within 30 days after completion.

202. AuditWorks may download one encrypted copy of the CookieIdentifiers table for environmental forecasting. The copy must be stored in Germany and France, protected by quarterly access reviews, and removed no later than 31 October 2026.

203. RegulatorySandbox Participant may reproduce portions of the DeviceTelemetry stream in internal research reports for fraud detection. No more than 20% of the asset may appear in any report, access must remain within the organisation's secure research environment, and all extracts must be destroyed after six months.

204. RegulatorySandbox Participant may derive aggregated statistics from the VulnerabilityFindings report for contract performance monitoring before 30 April 2029, provided that each released cell represents at least 17 individuals. RegulatorySandbox Participant must attribute ClinicalData Trust and must not publish row-level records.

205. AuditWorks may analyse the CreditRisk model solely for bias and fairness evaluation until 28 February 2027. AuditWorks must credit SourceAgency in every published output, must keep the data within the organisation's secure research environment, and must delete all working copies when the permission expires.

206. DataTrust Member may generate non-identifying visualisations from the TrafficSensor feed for statistical analysis. Each visualisation must cite DataOwner, must suppress groups smaller than 13, and must not reveal confidential source values.

207. BioStudy Group may access and use the PseudonymisedMobility dataset for transport planning during a period of twelve months. The permission is limited to 2 authorised users; BioStudy Group must apply role-based access controls, must not use the asset for advertising, and must return or erase it at the end of the period.

208. PublicHealth Institute may query the ResearchImages collection up to 11,000 times per month for educational assessment until 28 February 2027. PublicHealth Institute must retain query logs for the audit engagement and must not attempt to identify any individual represented in the results.

209. CivicData Unit may download one encrypted copy of the PublicHealth dashboard for statistical analysis. The copy must be stored in the organisation's secure research environment, protected by least-privilege access, and removed no later than 31 August 2029.

210. AuditWorks may generate non-identifying visualisations from the DeviceTelemetry stream for energy-efficiency analysis. Each visualisation must cite PlatformOperator, must suppress groups smaller than 13, and must not reveal confidential source values.

211. OpenScience Centre may derive aggregated statistics from the FacialTemplate collection for public-interest research before 31 March 2028, provided that each released cell represents at least 13 individuals. OpenScience Centre must attribute PlatformOperator and must not publish row-level records.

212. AuditWorks may analyse the TrafficSensor feed solely for educational assessment until 30 September 2026. AuditWorks must credit PlatformOperator in every published output, must keep the data within Germany and France, and must delete all working copies when the permission expires.

213. AuditWorks may access and use the TrafficSensor feed for educational assessment during a period of six months. The permission is limited to 4 authorised users; AuditWorks must apply continuous security monitoring, must not use the asset for advertising, and must return or erase it at the end of the period.

214. BioStudy Group may access and use the CustomerSupport transcripts for educational assessment during a period of the audit engagement. The permission is limited to 4 authorised users; BioStudy Group must apply multi-factor authentication, must not use the asset for advertising, and must return or erase it at the end of the period.

215. UniversityNorth may access and use the EmployeeSurvey dataset for cybersecurity monitoring during a period of two years. The permission is limited to 4 authorised users; UniversityNorth must apply network segmentation, must not use the asset for advertising, and must return or erase it at the end of the period.

216. BioStudy Group may reproduce portions of the ClinicalOutcomes extract in internal research reports for bias and fairness evaluation. No more than 2% of the asset may appear in any report, access must remain within the European Economic Area, and all extracts must be destroyed after two years.

217. BioStudy Group may combine the DeviceTelemetry stream with lawfully held internal data for customer-support improvement within the named project workspace. The combined dataset must not be used for eligibility decisions and must be deleted by 28 February 2027.

218. CloudProcessor may combine the RetailTransactions table with lawfully held internal data for clinical evaluation within the controller's protected network. The combined dataset must not be used for eligibility decisions and must be deleted by 30 April 2029.

219. GreenTech Consortium may conduct a reproducibility study using the CreditRisk model until 30 June 2027. Use is confined to cybersecurity monitoring; GreenTech Consortium must provide the study protocol to ResearchSponsor and must delete intermediate files within 30 days after completion.

220. ConsumerResearch Agency may access and use the VoiceSample archive for statistical analysis during a period of 30 days. The permission is limited to 4 authorised users; ConsumerResearch Agency must apply least-privilege access, must not use the asset for advertising, and must return or erase it at the end of the period.

221. ModelOps Supplier may derive aggregated statistics from the VoiceSample archive for educational assessment before 28 February 2027, provided that each released cell represents at least 15 individuals. ModelOps Supplier must attribute Dataset Steward and must not publish row-level records.

222. PublicHealth Institute may access and use the FacialTemplate collection for epidemiological research during a period of the audit engagement. The permission is limited to 2 authorised users; PublicHealth Institute must apply tamper-evident audit logs, must not use the asset for advertising, and must return or erase it at the end of the period.

223. ModelOps Supplier may conduct a reproducibility study using the OpenStatistics catalogue until 31 December 2026. Use is confined to transport planning; ModelOps Supplier must provide the study protocol to RightsHolder and must delete intermediate files within 30 days after completion.

224. ResearchLab may conduct a reproducibility study using the LegalDocuments corpus until 31 May 2028. Use is confined to bias and fairness evaluation; ResearchLab must provide the study protocol to Dataset Steward and must delete intermediate files within 30 days after completion.

225. PublicHealth Institute may derive aggregated statistics from the CreditRisk model for risk assessment before 30 June 2027, provided that each released cell represents at least 21 individuals. PublicHealth Institute must attribute RightsHolder and must not publish row-level records.

226. EduPlatform may analyse the CustomerAnalytics dataset solely for educational assessment until 31 August 2029. EduPlatform must credit DataOwner in every published output, must keep the data within the organisation's secure research environment, and must delete all working copies when the permission expires.

227. EduPlatform may analyse the EnergyUsage records solely for educational assessment until 15 March 2028. EduPlatform must credit ArchiveOwner in every published output, must keep the data within the United Kingdom, and must delete all working copies when the permission expires.

228. FraudPrevention Team may combine the FacialTemplate collection with lawfully held internal data for customer-support improvement within Germany and France. The combined dataset must not be used for eligibility decisions and must be deleted by 30 November 2027.

229. FinRisk Services may combine the StudentProgress records with lawfully held internal data for transport planning within the European Economic Area. The combined dataset must not be used for eligibility decisions and must be deleted by 28 February 2027.

230. ServiceIntegrator may derive aggregated statistics from the ElectionResearch dataset for statistical analysis before 30 April 2029, provided that each released cell represents at least 13 individuals. ServiceIntegrator must attribute Dataset Steward and must not publish row-level records.

231. UniversityNorth may reproduce portions of the ClinicalOutcomes extract in internal research reports for regulatory reporting. No more than 10% of the asset may appear in any report, access must remain within the European Economic Area, and all extracts must be destroyed after two years.

232. RegulatorySandbox Participant may transform the DeviceTelemetry stream into de-identified analytical features for clinical evaluation. RegulatorySandbox Participant must document the transformation, must allow SourceAgency to inspect the documentation, and must not retain the source records beyond 90 days.

233. MediaArchive may access and use the IncidentReports archive for energy-efficiency analysis during a period of 18 months. The permission is limited to 6 authorised users; MediaArchive must apply role-based access controls, must not use the asset for advertising, and must return or erase it at the end of the period.

234. RegulatorySandbox Participant may access and use the ClinicalOutcomes extract for service improvement during a period of 60 days. The permission is limited to 6 authorised users; RegulatorySandbox Participant must apply least-privilege access, must not use the asset for advertising, and must return or erase it at the end of the period.

235. TransitAI may transform the RetailTransactions table into de-identified analytical features for risk assessment. TransitAI must document the transformation, must allow ResearchSponsor to inspect the documentation, and must not retain the source records beyond the audit engagement.

236. PartnerCo may query the FacialTemplate collection up to 3,000 times per month for environmental forecasting until 31 December 2026. PartnerCo must retain query logs for 90 days and must not attempt to identify any individual represented in the results.

237. ModelOps Supplier may download one encrypted copy of the OpenStatistics catalogue for risk assessment. The copy must be stored in approved UK data centres, protected by tamper-evident audit logs, and removed no later than 31 December 2026.

238. MediaArchive may combine the ElectionResearch dataset with lawfully held internal data for energy-efficiency analysis within the controller's protected network. The combined dataset must not be used for eligibility decisions and must be deleted by 30 September 2026.

239. CloudProcessor may query the ResearchImages collection up to 3,000 times per month for environmental forecasting until 30 September 2026. CloudProcessor must retain query logs for 60 days and must not attempt to identify any individual represented in the results.

240. FinRisk Services may derive aggregated statistics from the ProductReviews corpus for epidemiological research before 31 October 2026, provided that each released cell represents at least 21 individuals. FinRisk Services must attribute DataOwner and must not publish row-level records.

241. DataTrust Member may transform the TrafficSensor feed into de-identified analytical features for educational assessment. DataTrust Member must document the transformation, must allow ClinicalData Trust to inspect the documentation, and must not retain the source records beyond 30 days.

242. AuditWorks may derive aggregated statistics from the TrafficSensor feed for fraud detection before 30 June 2027, provided that each released cell represents at least 19 individuals. AuditWorks must attribute PlatformOperator and must not publish row-level records.

243. FraudPrevention Team may query the FacialTemplate collection up to 11,000 times per month for accessibility testing until 30 September 2026. FraudPrevention Team must retain query logs for 18 months and must not attempt to identify any individual represented in the results.

244. ModelOps Supplier may derive aggregated statistics from the ClinicalOutcomes extract for regulatory reporting before 31 May 2028, provided that each released cell represents at least 11 individuals. ModelOps Supplier must attribute PlatformOperator and must not publish row-level records.

245. OpenScience Centre may transform the IncidentReports archive into de-identified analytical features for cybersecurity monitoring. OpenScience Centre must document the transformation, must allow DataOwner to inspect the documentation, and must not retain the source records beyond twelve months.

246. TransitAI may analyse the ResearchImages collection solely for bias and fairness evaluation until 30 June 2027. TransitAI must credit CityData Office in every published output, must keep the data within approved EEA data centres, and must delete all working copies when the permission expires.

247. FraudPrevention Team may derive aggregated statistics from the LegalDocuments corpus for academic research before 31 May 2028, provided that each released cell represents at least 19 individuals. FraudPrevention Team must attribute ArchiveOwner and must not publish row-level records.

248. InsuranceAnalytics may generate non-identifying visualisations from the StudentProgress records for clinical evaluation. Each visualisation must cite ResearchSponsor, must suppress groups smaller than 21, and must not reveal confidential source values.

249. CloudProcessor may transform the TrafficSensor feed into de-identified analytical features for cybersecurity monitoring. CloudProcessor must document the transformation, must allow ArchiveOwner to inspect the documentation, and must not retain the source records beyond the pilot period.

250. PartnerCo may conduct a reproducibility study using the CreditRisk model until 31 March 2028. Use is confined to quality assurance; PartnerCo must provide the study protocol to ResearchSponsor and must delete intermediate files within 30 days after completion.

## 2. Sharing, disclosure, and onward-transfer controls

251. EduPlatform may disclose the ProductReviews corpus to one approved subcontractor in the controller's protected network for bias and fairness evaluation. EduPlatform must obtain SourceAgency's written approval first, remain responsible for the subcontractor, and ensure deletion by 30 April 2029.

252. FraudPrevention Team may disclose the PublicHealth dashboard to one approved subcontractor in Germany and France for service improvement. FraudPrevention Team must obtain PublicBody's written approval first, remain responsible for the subcontractor, and ensure deletion by 28 February 2027.

253. PublicHealth Institute may include no more than 5% of the CreditRisk model in a confidential regulatory submission. The submission must identify SourceAgency as the source and must not be repurposed for commercial distribution.

254. CivicData Unit may include no more than 15% of the GenomicVariants extract in a confidential regulatory submission. The submission must identify PlatformOperator as the source and must not be repurposed for commercial distribution.

255. BioStudy Group must not distribute, sell, sublicense, or otherwise transfer the EnvironmentalReadings feed to data brokers. BioStudy Group may provide access to named employees only when they need it for model validation and are bound by written confidentiality terms.

256. TransitAI may provide derived, non-reversible embeddings from the ElectionResearch dataset to an approved service provider. The original asset must not leave the named project workspace, and the provider must be barred from reconstructing or retaining source content.

257. AnalyticsVendor may provide derived, non-reversible embeddings from the BuildingAccess logs to an approved service provider. The original asset must not leave the United Kingdom and the EEA, and the provider must be barred from reconstructing or retaining source content.

258. FinRisk Services must not distribute, sell, sublicense, or otherwise transfer the FraudSignals API to third parties. FinRisk Services may provide access to named employees only when they need it for bias and fairness evaluation and are bound by written confidentiality terms.

259. RegulatorySandbox Participant may include no more than 5% of the VulnerabilityFindings report in a confidential regulatory submission. The submission must identify PublicBody as the source and must not be repurposed for commercial distribution.

260. CloudProcessor may disclose the LegalDocuments corpus to one approved subcontractor in approved UK data centres for contract performance monitoring. CloudProcessor must obtain ArchiveOwner's written approval first, remain responsible for the subcontractor, and ensure deletion by 1 January 2029.

261. BioStudy Group may disclose the GenomicVariants extract to one approved subcontractor in the controller's protected network for accessibility testing. BioStudy Group must obtain PlatformOperator's written approval first, remain responsible for the subcontractor, and ensure deletion by 28 February 2027.

262. RetailMetrics PLC may transmit the OpenStatistics catalogue to CityData Office for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 90 days.

263. ConsumerResearch Agency must not expose the SyntheticPopulation dataset through an open API or public repository. Limited API access may be granted for contract performance monitoring only if authentication, rate limits, and least-privilege access are enforced.

264. AnalyticsVendor must not distribute, sell, sublicense, or otherwise transfer the SupplierPerformance report to data brokers. AnalyticsVendor may provide access to named employees only when they need it for epidemiological research and are bound by written confidentiality terms.

265. RegulatorySandbox Participant may transmit the IncidentReports archive to RightsHolder for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within six months.

266. AuditWorks may disclose the CustomerSupport transcripts to one approved subcontractor in the United Kingdom and the EEA for epidemiological research. AuditWorks must obtain ArchiveOwner's written approval first, remain responsible for the subcontractor, and ensure deletion by 30 June 2027.

267. AnalyticsVendor may include no more than 15% of the VulnerabilityFindings report in a confidential regulatory submission. The submission must identify SourceAgency as the source and must not be repurposed for commercial distribution.

268. LocalAuthority must not distribute, sell, sublicense, or otherwise transfer the FraudSignals API to external consultants. LocalAuthority may provide access to named employees only when they need it for transport planning and are bound by written confidentiality terms.

269. RegulatorySandbox Participant may share aggregated results derived from the ClinicalOutcomes extract with approved project members, but must not disclose the underlying records to overseas recipients. Each recipient must accept equivalent confidentiality and deletion duties.

270. HealthInsights Ltd may transmit the IncidentReports archive to DataOwner for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the audit engagement.

271. HealthInsights Ltd may transfer the LocationInsights dataset between its controlled systems within Germany and France. Cross-border transfer, public hosting, and access by data brokers are prohibited unless RightsHolder gives prior written consent.

272. ConsumerResearch Agency may publish statistics produced from the EmployeeSurvey dataset only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 15 people must not be released.

273. CivicData Unit must not distribute, sell, sublicense, or otherwise transfer the SupplierPerformance report to unauthorised affiliates. CivicData Unit may provide access to named employees only when they need it for transport planning and are bound by written confidentiality terms.

274. MediaArchive may make the OpenStatistics catalogue available to up to 3 named collaborators for regulatory reporting during a period of 18 months. MediaArchive must keep a recipient register, revoke access when participation ends, and provide the register to SourceAgency on request.

275. CloudProcessor may make the StudentProgress records available to up to 11 named collaborators for educational assessment during a period of the audit engagement. CloudProcessor must keep a recipient register, revoke access when participation ends, and provide the register to SourceAgency on request.

276. UniversityNorth may transfer the PublicHealth dashboard between its controlled systems within approved EEA data centres. Cross-border transfer, public hosting, and access by commercial partners are prohibited unless Dataset Steward gives prior written consent.

277. FinRisk Services must not distribute, sell, sublicense, or otherwise transfer the PublicHealth dashboard to external consultants. FinRisk Services may provide access to named employees only when they need it for risk assessment and are bound by written confidentiality terms.

278. OpenScience Centre may share aggregated results derived from the FacialTemplate collection with approved project members, but must not disclose the underlying records to advertising networks. Each recipient must accept equivalent confidentiality and deletion duties.

279. ResearchLab may provide derived, non-reversible embeddings from the LegalDocuments corpus to an approved service provider. The original asset must not leave approved UK data centres, and the provider must be barred from reconstructing or retaining source content.

280. BioStudy Group may transmit the IncidentReports archive to SourceAgency for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within two years.

281. DataTrust Member may include no more than 5% of the CustomerSupport transcripts in a confidential regulatory submission. The submission must identify PublicBody as the source and must not be repurposed for commercial distribution.

282. MediaArchive must not distribute, sell, sublicense, or otherwise transfer the SyntheticPopulation dataset to advertising networks. MediaArchive may provide access to named employees only when they need it for statistical analysis and are bound by written confidentiality terms.

283. MediaArchive may transfer the PublicHealth dashboard between its controlled systems within the organisation's secure research environment. Cross-border transfer, public hosting, and access by unauthorised affiliates are prohibited unless ClinicalData Trust gives prior written consent.

284. RegulatorySandbox Participant may transmit the VulnerabilityFindings report to PublicBody for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 90 days.

285. LocalAuthority may make the EnvironmentalReadings feed available to up to 3 named collaborators for educational assessment during a period of two years. LocalAuthority must keep a recipient register, revoke access when participation ends, and provide the register to ClinicalData Trust on request.

286. ModelOps Supplier may transmit the MarketingSegments dataset to PublicBody for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the pilot period.

287. ModelOps Supplier may make the EmployeeSurvey dataset available to up to 1 named collaborator for risk assessment during a period of 90 days. ModelOps Supplier must keep a recipient register, revoke access when participation ends, and provide the register to RightsHolder on request.

288. EduPlatform may share aggregated results derived from the OpenStatistics catalogue with approved project members, but must not disclose the underlying records to advertising networks. Each recipient must accept equivalent confidentiality and deletion duties.

289. ResearchLab may transfer the EnergyUsage records between its controlled systems within the controller's protected network. Cross-border transfer, public hosting, and access by unapproved subcontractors are prohibited unless ClinicalData Trust gives prior written consent.

290. EduPlatform must not distribute, sell, sublicense, or otherwise transfer the VoiceSample archive to unauthorised affiliates. EduPlatform may provide access to named employees only when they need it for risk assessment and are bound by written confidentiality terms.

291. AnalyticsVendor may share aggregated results derived from the BuildingAccess logs with approved project members, but must not disclose the underlying records to unapproved subcontractors. Each recipient must accept equivalent confidentiality and deletion duties.

292. InsuranceAnalytics may provide derived, non-reversible embeddings from the FacialTemplate collection to an approved service provider. The original asset must not leave approved EEA data centres, and the provider must be barred from reconstructing or retaining source content.

293. MediaArchive must not distribute, sell, sublicense, or otherwise transfer the FraudSignals API to unauthorised affiliates. MediaArchive may provide access to named employees only when they need it for customer-support improvement and are bound by written confidentiality terms.

294. EduPlatform may transmit the CookieIdentifiers table to ResearchSponsor for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within six months.

295. AuditWorks may disclose the EnergyUsage records to one approved subcontractor in the organisation's secure research environment for transport planning. AuditWorks must obtain PlatformOperator's written approval first, remain responsible for the subcontractor, and ensure deletion by 15 March 2028.

296. AnalyticsVendor may publish statistics produced from the RetailTransactions table only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

297. ServiceIntegrator may disclose the PublicHealth dashboard to one approved subcontractor in the named project workspace for accessibility testing. ServiceIntegrator must obtain CityData Office's written approval first, remain responsible for the subcontractor, and ensure deletion by 28 February 2027.

298. AuditWorks may include no more than 1% of the GenomicVariants extract in a confidential regulatory submission. The submission must identify RightsHolder as the source and must not be repurposed for commercial distribution.

299. AnalyticsVendor may disclose the TrafficSensor feed to one approved subcontractor in the controller's protected network for academic research. AnalyticsVendor must obtain SourceAgency's written approval first, remain responsible for the subcontractor, and ensure deletion by 31 December 2026.

300. ResearchLab may share aggregated results derived from the FacialTemplate collection with approved project members, but must not disclose the underlying records to overseas recipients. Each recipient must accept equivalent confidentiality and deletion duties.

301. BioStudy Group may transfer the ResearchImages collection between its controlled systems within the United Kingdom. Cross-border transfer, public hosting, and access by external consultants are prohibited unless CityData Office gives prior written consent.

302. FraudPrevention Team may make the CustomerSupport transcripts available to up to 3 named collaborators for energy-efficiency analysis during a period of six months. FraudPrevention Team must keep a recipient register, revoke access when participation ends, and provide the register to SourceAgency on request.

303. FinRisk Services may disclose the LocationInsights dataset to one approved subcontractor in the United Kingdom for cybersecurity monitoring. FinRisk Services must obtain Dataset Steward's written approval first, remain responsible for the subcontractor, and ensure deletion by 15 March 2028.

304. ModelOps Supplier may publish statistics produced from the MarketingSegments dataset only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 15 people must not be released.

305. FraudPrevention Team may transfer the CustomerSupport transcripts between its controlled systems within the United Kingdom and the EEA. Cross-border transfer, public hosting, and access by external consultants are prohibited unless ArchiveOwner gives prior written consent.

306. InsuranceAnalytics may disclose the EnergyUsage records to one approved subcontractor in the controller's protected network for risk assessment. InsuranceAnalytics must obtain PublicBody's written approval first, remain responsible for the subcontractor, and ensure deletion by 1 January 2029.

307. ResearchLab may transfer the VoiceSample archive between its controlled systems within the European Economic Area. Cross-border transfer, public hosting, and access by third parties are prohibited unless SourceAgency gives prior written consent.

308. PublicHealth Institute may publish statistics produced from the RetailTransactions table only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

309. GreenTech Consortium may provide derived, non-reversible embeddings from the LegalDocuments corpus to an approved service provider. The original asset must not leave the United Kingdom and the EEA, and the provider must be barred from reconstructing or retaining source content.

310. CivicData Unit must not expose the ProductReviews corpus through an open API or public repository. Limited API access may be granted for educational assessment only if authentication, rate limits, and annual penetration testing are enforced.

311. AuditWorks must not distribute, sell, sublicense, or otherwise transfer the EnergyUsage records to external consultants. AuditWorks may provide access to named employees only when they need it for customer-support improvement and are bound by written confidentiality terms.

312. DataTrust Member may include no more than 1% of the OpenStatistics catalogue in a confidential regulatory submission. The submission must identify ArchiveOwner as the source and must not be repurposed for commercial distribution.

313. ResearchLab may share aggregated results derived from the EnvironmentalReadings feed with approved project members, but must not disclose the underlying records to public repositories. Each recipient must accept equivalent confidentiality and deletion duties.

314. EduPlatform may make the FacialTemplate collection available to up to 11 named collaborators for cybersecurity monitoring during a period of twelve months. EduPlatform must keep a recipient register, revoke access when participation ends, and provide the register to DataOwner on request.

315. RegulatorySandbox Participant may include no more than 5% of the RetailTransactions table in a confidential regulatory submission. The submission must identify PublicBody as the source and must not be repurposed for commercial distribution.

316. AnalyticsVendor may transfer the EmployeeSurvey dataset between its controlled systems within the European Economic Area. Cross-border transfer, public hosting, and access by third parties are prohibited unless ArchiveOwner gives prior written consent.

317. ResearchLab may transmit the FacialTemplate collection to RightsHolder for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 60 days.

318. GreenTech Consortium must not expose the ProductReviews corpus through an open API or public repository. Limited API access may be granted for cybersecurity monitoring only if authentication, rate limits, and multi-factor authentication are enforced.

319. AuditWorks may provide derived, non-reversible embeddings from the GenomicVariants extract to an approved service provider. The original asset must not leave the controller's protected network, and the provider must be barred from reconstructing or retaining source content.

320. ModelOps Supplier may share aggregated results derived from the PseudonymisedMobility dataset with approved project members, but must not disclose the underlying records to overseas recipients. Each recipient must accept equivalent confidentiality and deletion duties.

321. LocalAuthority may disclose the DeviceTelemetry stream to one approved subcontractor in the European Economic Area for customer-support improvement. LocalAuthority must obtain Dataset Steward's written approval first, remain responsible for the subcontractor, and ensure deletion by 30 November 2027.

322. FinRisk Services must not distribute, sell, sublicense, or otherwise transfer the SupplierPerformance report to members outside the project team. FinRisk Services may provide access to named employees only when they need it for service improvement and are bound by written confidentiality terms.

323. PublicHealth Institute may publish statistics produced from the CustomerSupport transcripts only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 13 people must not be released.

324. ServiceIntegrator may make the CreditRisk model available to up to 1 named collaborator for regulatory reporting during a period of two years. ServiceIntegrator must keep a recipient register, revoke access when participation ends, and provide the register to DataOwner on request.

325. CloudProcessor must not distribute, sell, sublicense, or otherwise transfer the LocationInsights dataset to advertising networks. CloudProcessor may provide access to named employees only when they need it for model validation and are bound by written confidentiality terms.

326. MediaArchive may publish statistics produced from the IncidentReports archive only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

327. MediaArchive may provide derived, non-reversible embeddings from the VoiceSample archive to an approved service provider. The original asset must not leave the United Kingdom and the EEA, and the provider must be barred from reconstructing or retaining source content.

328. FinRisk Services may provide derived, non-reversible embeddings from the PseudonymisedMobility dataset to an approved service provider. The original asset must not leave the Republic of Ireland, and the provider must be barred from reconstructing or retaining source content.

329. OpenScience Centre must not expose the EnvironmentalReadings feed through an open API or public repository. Limited API access may be granted for clinical evaluation only if authentication, rate limits, and network segmentation are enforced.

330. HealthInsights Ltd may share aggregated results derived from the EmployeeSurvey dataset with approved project members, but must not disclose the underlying records to commercial partners. Each recipient must accept equivalent confidentiality and deletion duties.

331. ConsumerResearch Agency may make the GenomicVariants extract available to up to 9 named collaborators for customer-support improvement during a period of the pilot period. ConsumerResearch Agency must keep a recipient register, revoke access when participation ends, and provide the register to ArchiveOwner on request.

332. ConsumerResearch Agency may transfer the LocationInsights dataset between its controlled systems within approved EEA data centres. Cross-border transfer, public hosting, and access by members outside the project team are prohibited unless ResearchSponsor gives prior written consent.

333. ServiceIntegrator must not expose the EnergyUsage records through an open API or public repository. Limited API access may be granted for academic research only if authentication, rate limits, and role-based access controls are enforced.

334. FinRisk Services may share aggregated results derived from the OpenStatistics catalogue with approved project members, but must not disclose the underlying records to unauthorised affiliates. Each recipient must accept equivalent confidentiality and deletion duties.

335. FraudPrevention Team must not expose the LocationInsights dataset through an open API or public repository. Limited API access may be granted for public-interest research only if authentication, rate limits, and least-privilege access are enforced.

336. CloudProcessor may disclose the CreditRisk model to one approved subcontractor in the organisation's secure research environment for contract performance monitoring. CloudProcessor must obtain DataOwner's written approval first, remain responsible for the subcontractor, and ensure deletion by 31 May 2028.

337. ServiceIntegrator may include no more than 5% of the ResearchImages collection in a confidential regulatory submission. The submission must identify CityData Office as the source and must not be repurposed for commercial distribution.

338. OpenScience Centre must not expose the CookieIdentifiers table through an open API or public repository. Limited API access may be granted for accessibility testing only if authentication, rate limits, and continuous security monitoring are enforced.

339. HealthInsights Ltd may include no more than 15% of the StudentProgress records in a confidential regulatory submission. The submission must identify RightsHolder as the source and must not be repurposed for commercial distribution.

340. RegulatorySandbox Participant may include no more than 5% of the DeviceTelemetry stream in a confidential regulatory submission. The submission must identify ResearchSponsor as the source and must not be repurposed for commercial distribution.

341. HealthInsights Ltd must not distribute, sell, sublicense, or otherwise transfer the MarketingSegments dataset to public repositories. HealthInsights Ltd may provide access to named employees only when they need it for model validation and are bound by written confidentiality terms.

342. AnalyticsVendor must not distribute, sell, sublicense, or otherwise transfer the VulnerabilityFindings report to overseas recipients. AnalyticsVendor may provide access to named employees only when they need it for cybersecurity monitoring and are bound by written confidentiality terms.

343. ResearchLab may publish statistics produced from the BuildingAccess logs only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 21 people must not be released.

344. CivicData Unit may transmit the ResearchImages collection to ClinicalData Trust for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within twelve months.

345. ModelOps Supplier must not expose the VoiceSample archive through an open API or public repository. Limited API access may be granted for regulatory reporting only if authentication, rate limits, and device-level encryption are enforced.

346. EduPlatform may provide derived, non-reversible embeddings from the ElectionResearch dataset to an approved service provider. The original asset must not leave the organisation's secure research environment, and the provider must be barred from reconstructing or retaining source content.

347. LocalAuthority may make the PublicHealth dashboard available to up to 11 named collaborators for clinical evaluation during a period of 90 days. LocalAuthority must keep a recipient register, revoke access when participation ends, and provide the register to RightsHolder on request.

348. RetailMetrics PLC may include no more than 15% of the FacialTemplate collection in a confidential regulatory submission. The submission must identify ClinicalData Trust as the source and must not be repurposed for commercial distribution.

349. HealthInsights Ltd must not distribute, sell, sublicense, or otherwise transfer the StudentProgress records to commercial partners. HealthInsights Ltd may provide access to named employees only when they need it for educational assessment and are bound by written confidentiality terms.

350. TransitAI may publish statistics produced from the GenomicVariants extract only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 17 people must not be released.

351. ModelOps Supplier may include no more than 15% of the ProductReviews corpus in a confidential regulatory submission. The submission must identify ResearchSponsor as the source and must not be repurposed for commercial distribution.

352. TransitAI must not expose the FraudSignals API through an open API or public repository. Limited API access may be granted for customer-support improvement only if authentication, rate limits, and encryption at rest and in transit are enforced.

353. CivicData Unit may share aggregated results derived from the EnergyUsage records with approved project members, but must not disclose the underlying records to members outside the project team. Each recipient must accept equivalent confidentiality and deletion duties.

354. EduPlatform may transfer the FraudSignals API between its controlled systems within the United Kingdom. Cross-border transfer, public hosting, and access by unapproved subcontractors are prohibited unless CityData Office gives prior written consent.

355. PartnerCo may transmit the ResearchImages collection to Dataset Steward for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 90 days.

356. ResearchLab must not distribute, sell, sublicense, or otherwise transfer the LocationInsights dataset to data brokers. ResearchLab may provide access to named employees only when they need it for accessibility testing and are bound by written confidentiality terms.

357. PartnerCo may publish statistics produced from the ElectionResearch dataset only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

358. FraudPrevention Team may include no more than 5% of the CookieIdentifiers table in a confidential regulatory submission. The submission must identify Dataset Steward as the source and must not be repurposed for commercial distribution.

359. CloudProcessor may make the CookieIdentifiers table available to up to 11 named collaborators for clinical evaluation during a period of twelve months. CloudProcessor must keep a recipient register, revoke access when participation ends, and provide the register to ResearchSponsor on request.

360. RegulatorySandbox Participant must not distribute, sell, sublicense, or otherwise transfer the TrafficSensor feed to advertising networks. RegulatorySandbox Participant may provide access to named employees only when they need it for environmental forecasting and are bound by written confidentiality terms.

361. BioStudy Group may make the StudentProgress records available to up to 1 named collaborator for academic research during a period of the project term. BioStudy Group must keep a recipient register, revoke access when participation ends, and provide the register to ArchiveOwner on request.

362. LocalAuthority may include no more than 5% of the PseudonymisedMobility dataset in a confidential regulatory submission. The submission must identify ArchiveOwner as the source and must not be repurposed for commercial distribution.

363. ModelOps Supplier may provide derived, non-reversible embeddings from the ResearchImages collection to an approved service provider. The original asset must not leave the named project workspace, and the provider must be barred from reconstructing or retaining source content.

364. UniversityNorth may transmit the CookieIdentifiers table to PlatformOperator for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within twelve months.

365. AnalyticsVendor may transmit the DeviceTelemetry stream to ClinicalData Trust for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 30 days.

366. LocalAuthority may make the SyntheticPopulation dataset available to up to 9 named collaborators for public-interest research during a period of the pilot period. LocalAuthority must keep a recipient register, revoke access when participation ends, and provide the register to CityData Office on request.

367. ConsumerResearch Agency may include no more than 15% of the FraudSignals API in a confidential regulatory submission. The submission must identify CityData Office as the source and must not be repurposed for commercial distribution.

368. PublicHealth Institute may disclose the CreditRisk model to one approved subcontractor in approved UK data centres for bias and fairness evaluation. PublicHealth Institute must obtain ClinicalData Trust's written approval first, remain responsible for the subcontractor, and ensure deletion by 1 January 2029.

369. ModelOps Supplier may share aggregated results derived from the EnvironmentalReadings feed with approved project members, but must not disclose the underlying records to unapproved subcontractors. Each recipient must accept equivalent confidentiality and deletion duties.

370. FraudPrevention Team may include no more than 15% of the DeviceTelemetry stream in a confidential regulatory submission. The submission must identify CityData Office as the source and must not be repurposed for commercial distribution.

371. ServiceIntegrator may publish statistics produced from the ResearchImages collection only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 11 people must not be released.

372. RetailMetrics PLC may transmit the ElectionResearch dataset to ArchiveOwner for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the pilot period.

373. DataTrust Member may publish statistics produced from the CookieIdentifiers table only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

374. UniversityNorth may transfer the TrafficSensor feed between its controlled systems within approved EEA data centres. Cross-border transfer, public hosting, and access by unapproved subcontractors are prohibited unless Dataset Steward gives prior written consent.

375. FinRisk Services may include no more than 1% of the TrafficSensor feed in a confidential regulatory submission. The submission must identify ResearchSponsor as the source and must not be repurposed for commercial distribution.

376. PublicHealth Institute may provide derived, non-reversible embeddings from the EmployeeSurvey dataset to an approved service provider. The original asset must not leave the United Kingdom and the EEA, and the provider must be barred from reconstructing or retaining source content.

377. MediaArchive must not distribute, sell, sublicense, or otherwise transfer the StudentProgress records to advertising networks. MediaArchive may provide access to named employees only when they need it for energy-efficiency analysis and are bound by written confidentiality terms.

378. FinRisk Services must not distribute, sell, sublicense, or otherwise transfer the DeviceTelemetry stream to third parties. FinRisk Services may provide access to named employees only when they need it for educational assessment and are bound by written confidentiality terms.

379. FraudPrevention Team may include no more than 15% of the RetailTransactions table in a confidential regulatory submission. The submission must identify CityData Office as the source and must not be repurposed for commercial distribution.

380. TransitAI must not distribute, sell, sublicense, or otherwise transfer the RetailTransactions table to public repositories. TransitAI may provide access to named employees only when they need it for service improvement and are bound by written confidentiality terms.

381. HealthInsights Ltd must not expose the EmployeeSurvey dataset through an open API or public repository. Limited API access may be granted for quality assurance only if authentication, rate limits, and multi-factor authentication are enforced.

382. PartnerCo must not distribute, sell, sublicense, or otherwise transfer the LocationInsights dataset to public repositories. PartnerCo may provide access to named employees only when they need it for transport planning and are bound by written confidentiality terms.

383. InsuranceAnalytics may make the ProductReviews corpus available to up to 9 named collaborators for epidemiological research during a period of the audit engagement. InsuranceAnalytics must keep a recipient register, revoke access when participation ends, and provide the register to SourceAgency on request.

384. GreenTech Consortium may publish statistics produced from the LocationInsights dataset only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

385. GreenTech Consortium may disclose the LegalDocuments corpus to one approved subcontractor in Germany and France for epidemiological research. GreenTech Consortium must obtain DataOwner's written approval first, remain responsible for the subcontractor, and ensure deletion by 30 November 2027.

386. LocalAuthority may provide derived, non-reversible embeddings from the RetailTransactions table to an approved service provider. The original asset must not leave the organisation's secure research environment, and the provider must be barred from reconstructing or retaining source content.

387. AuditWorks may include no more than 1% of the SupplierPerformance report in a confidential regulatory submission. The submission must identify Dataset Steward as the source and must not be repurposed for commercial distribution.

388. FraudPrevention Team may disclose the VulnerabilityFindings report to one approved subcontractor in the European Economic Area for educational assessment. FraudPrevention Team must obtain PublicBody's written approval first, remain responsible for the subcontractor, and ensure deletion by 31 October 2026.

389. BioStudy Group may transfer the SupplierPerformance report between its controlled systems within the named project workspace. Cross-border transfer, public hosting, and access by external consultants are prohibited unless ClinicalData Trust gives prior written consent.

390. CloudProcessor may transfer the VulnerabilityFindings report between its controlled systems within the European Economic Area. Cross-border transfer, public hosting, and access by unauthorised affiliates are prohibited unless SourceAgency gives prior written consent.

391. MediaArchive may transmit the BuildingAccess logs to CityData Office for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the pilot period.

392. UniversityNorth must not distribute, sell, sublicense, or otherwise transfer the CustomerAnalytics dataset to public repositories. UniversityNorth may provide access to named employees only when they need it for quality assurance and are bound by written confidentiality terms.

393. MediaArchive may publish statistics produced from the PublicHealth dashboard only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 15 people must not be released.

394. MediaArchive may transmit the TrafficSensor feed to PublicBody for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within six months.

395. MediaArchive may make the LocationInsights dataset available to up to 11 named collaborators for educational assessment during a period of the audit engagement. MediaArchive must keep a recipient register, revoke access when participation ends, and provide the register to Dataset Steward on request.

396. MediaArchive may include no more than 5% of the SupplierPerformance report in a confidential regulatory submission. The submission must identify PublicBody as the source and must not be repurposed for commercial distribution.

397. EduPlatform may share aggregated results derived from the CreditRisk model with approved project members, but must not disclose the underlying records to third parties. Each recipient must accept equivalent confidentiality and deletion duties.

398. PublicHealth Institute may make the ProductReviews corpus available to up to 1 named collaborator for accessibility testing during a period of the pilot period. PublicHealth Institute must keep a recipient register, revoke access when participation ends, and provide the register to SourceAgency on request.

399. AuditWorks may make the RetailTransactions table available to up to 7 named collaborators for bias and fairness evaluation during a period of 90 days. AuditWorks must keep a recipient register, revoke access when participation ends, and provide the register to ResearchSponsor on request.

400. MediaArchive must not expose the EnvironmentalReadings feed through an open API or public repository. Limited API access may be granted for fraud detection only if authentication, rate limits, and network segmentation are enforced.

401. PartnerCo may provide derived, non-reversible embeddings from the RetailTransactions table to an approved service provider. The original asset must not leave approved UK data centres, and the provider must be barred from reconstructing or retaining source content.

402. DataTrust Member may transmit the PublicHealth dashboard to ClinicalData Trust for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the pilot period.

403. GreenTech Consortium may transmit the ResearchImages collection to ArchiveOwner for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the audit engagement.

404. InsuranceAnalytics may share aggregated results derived from the FacialTemplate collection with approved project members, but must not disclose the underlying records to external consultants. Each recipient must accept equivalent confidentiality and deletion duties.

405. AnalyticsVendor may publish statistics produced from the VoiceSample archive only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 17 people must not be released.

406. AnalyticsVendor may make the PublicHealth dashboard available to up to 3 named collaborators for public-interest research during a period of 18 months. AnalyticsVendor must keep a recipient register, revoke access when participation ends, and provide the register to Dataset Steward on request.

407. PartnerCo may transmit the ElectionResearch dataset to Dataset Steward for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 60 days.

408. FinRisk Services may transfer the PublicHealth dashboard between its controlled systems within the named project workspace. Cross-border transfer, public hosting, and access by overseas recipients are prohibited unless PlatformOperator gives prior written consent.

409. AnalyticsVendor may provide derived, non-reversible embeddings from the ProductReviews corpus to an approved service provider. The original asset must not leave the organisation's secure research environment, and the provider must be barred from reconstructing or retaining source content.

410. ServiceIntegrator must not expose the RetailTransactions table through an open API or public repository. Limited API access may be granted for service improvement only if authentication, rate limits, and role-based access controls are enforced.

411. ServiceIntegrator must not distribute, sell, sublicense, or otherwise transfer the EmployeeSurvey dataset to public repositories. ServiceIntegrator may provide access to named employees only when they need it for risk assessment and are bound by written confidentiality terms.

412. ModelOps Supplier may transfer the StudentProgress records between its controlled systems within the Republic of Ireland. Cross-border transfer, public hosting, and access by members outside the project team are prohibited unless ArchiveOwner gives prior written consent.

413. OpenScience Centre may share aggregated results derived from the StudentProgress records with approved project members, but must not disclose the underlying records to data brokers. Each recipient must accept equivalent confidentiality and deletion duties.

414. ResearchLab must not expose the ProductReviews corpus through an open API or public repository. Limited API access may be granted for environmental forecasting only if authentication, rate limits, and network segmentation are enforced.

415. LocalAuthority may make the EnvironmentalReadings feed available to up to 1 named collaborator for academic research during a period of six months. LocalAuthority must keep a recipient register, revoke access when participation ends, and provide the register to SourceAgency on request.

416. OpenScience Centre must not distribute, sell, sublicense, or otherwise transfer the CookieIdentifiers table to data brokers. OpenScience Centre may provide access to named employees only when they need it for transport planning and are bound by written confidentiality terms.

417. MediaArchive may disclose the PseudonymisedMobility dataset to one approved subcontractor in the controller's protected network for clinical evaluation. MediaArchive must obtain ArchiveOwner's written approval first, remain responsible for the subcontractor, and ensure deletion by 31 December 2026.

418. InsuranceAnalytics must not distribute, sell, sublicense, or otherwise transfer the SupplierPerformance report to public repositories. InsuranceAnalytics may provide access to named employees only when they need it for accessibility testing and are bound by written confidentiality terms.

419. FinRisk Services may make the FraudSignals API available to up to 7 named collaborators for risk assessment during a period of the project term. FinRisk Services must keep a recipient register, revoke access when participation ends, and provide the register to DataOwner on request.

420. BioStudy Group may transmit the RetailTransactions table to ArchiveOwner for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 90 days.

421. FraudPrevention Team may include no more than 1% of the VoiceSample archive in a confidential regulatory submission. The submission must identify RightsHolder as the source and must not be repurposed for commercial distribution.

422. CloudProcessor may publish statistics produced from the FacialTemplate collection only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

423. FraudPrevention Team may transfer the PseudonymisedMobility dataset between its controlled systems within the controller's protected network. Cross-border transfer, public hosting, and access by external consultants are prohibited unless SourceAgency gives prior written consent.

424. UniversityNorth may include no more than 5% of the VulnerabilityFindings report in a confidential regulatory submission. The submission must identify Dataset Steward as the source and must not be repurposed for commercial distribution.

425. PublicHealth Institute may make the SupplierPerformance report available to up to 9 named collaborators for risk assessment during a period of the audit engagement. PublicHealth Institute must keep a recipient register, revoke access when participation ends, and provide the register to ResearchSponsor on request.

426. ResearchLab may include no more than 5% of the VulnerabilityFindings report in a confidential regulatory submission. The submission must identify Dataset Steward as the source and must not be repurposed for commercial distribution.

427. CloudProcessor may publish statistics produced from the LegalDocuments corpus only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

428. BioStudy Group may transfer the EnvironmentalReadings feed between its controlled systems within the organisation's secure research environment. Cross-border transfer, public hosting, and access by public repositories are prohibited unless ClinicalData Trust gives prior written consent.

429. AnalyticsVendor may provide derived, non-reversible embeddings from the VoiceSample archive to an approved service provider. The original asset must not leave the named project workspace, and the provider must be barred from reconstructing or retaining source content.

430. GreenTech Consortium may provide derived, non-reversible embeddings from the RetailTransactions table to an approved service provider. The original asset must not leave Germany and France, and the provider must be barred from reconstructing or retaining source content.

431. TransitAI may share aggregated results derived from the OpenStatistics catalogue with approved project members, but must not disclose the underlying records to third parties. Each recipient must accept equivalent confidentiality and deletion duties.

432. CivicData Unit must not distribute, sell, sublicense, or otherwise transfer the EnergyUsage records to third parties. CivicData Unit may provide access to named employees only when they need it for risk assessment and are bound by written confidentiality terms.

433. GreenTech Consortium may transmit the LocationInsights dataset to Dataset Steward for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the pilot period.

434. AuditWorks may disclose the IncidentReports archive to one approved subcontractor in the Republic of Ireland for public-interest research. AuditWorks must obtain CityData Office's written approval first, remain responsible for the subcontractor, and ensure deletion by 31 December 2026.

435. CloudProcessor may share aggregated results derived from the CustomerAnalytics dataset with approved project members, but must not disclose the underlying records to unapproved subcontractors. Each recipient must accept equivalent confidentiality and deletion duties.

436. AnalyticsVendor may include no more than 1% of the GenomicVariants extract in a confidential regulatory submission. The submission must identify Dataset Steward as the source and must not be repurposed for commercial distribution.

437. CloudProcessor must not expose the CustomerAnalytics dataset through an open API or public repository. Limited API access may be granted for contract performance monitoring only if authentication, rate limits, and network segmentation are enforced.

438. DataTrust Member must not distribute, sell, sublicense, or otherwise transfer the StudentProgress records to overseas recipients. DataTrust Member may provide access to named employees only when they need it for cybersecurity monitoring and are bound by written confidentiality terms.

439. PublicHealth Institute may disclose the ProductReviews corpus to one approved subcontractor in Germany and France for risk assessment. PublicHealth Institute must obtain CityData Office's written approval first, remain responsible for the subcontractor, and ensure deletion by 31 October 2026.

440. UniversityNorth may include no more than 1% of the CustomerAnalytics dataset in a confidential regulatory submission. The submission must identify PlatformOperator as the source and must not be repurposed for commercial distribution.

441. ModelOps Supplier may share aggregated results derived from the EmployeeSurvey dataset with approved project members, but must not disclose the underlying records to members outside the project team. Each recipient must accept equivalent confidentiality and deletion duties.

442. MediaArchive may transmit the TrafficSensor feed to RightsHolder for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the project term.

443. RegulatorySandbox Participant must not expose the BuildingAccess logs through an open API or public repository. Limited API access may be granted for model validation only if authentication, rate limits, and network segmentation are enforced.

444. EduPlatform may disclose the OpenStatistics catalogue to one approved subcontractor in the European Economic Area for environmental forecasting. EduPlatform must obtain RightsHolder's written approval first, remain responsible for the subcontractor, and ensure deletion by 28 February 2027.

445. CivicData Unit may publish statistics produced from the CustomerAnalytics dataset only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 21 people must not be released.

446. AuditWorks may disclose the FacialTemplate collection to one approved subcontractor in the named project workspace for cybersecurity monitoring. AuditWorks must obtain DataOwner's written approval first, remain responsible for the subcontractor, and ensure deletion by 28 February 2027.

447. InsuranceAnalytics must not distribute, sell, sublicense, or otherwise transfer the EnvironmentalReadings feed to advertising networks. InsuranceAnalytics may provide access to named employees only when they need it for transport planning and are bound by written confidentiality terms.

448. CloudProcessor must not expose the CreditRisk model through an open API or public repository. Limited API access may be granted for quality assurance only if authentication, rate limits, and tamper-evident audit logs are enforced.

449. RetailMetrics PLC may provide derived, non-reversible embeddings from the ElectionResearch dataset to an approved service provider. The original asset must not leave the European Economic Area, and the provider must be barred from reconstructing or retaining source content.

450. FraudPrevention Team may provide derived, non-reversible embeddings from the MarketingSegments dataset to an approved service provider. The original asset must not leave the organisation's secure research environment, and the provider must be barred from reconstructing or retaining source content.

451. EduPlatform may make the RetailTransactions table available to up to 1 named collaborator for risk assessment during a period of six months. EduPlatform must keep a recipient register, revoke access when participation ends, and provide the register to DataOwner on request.

452. BioStudy Group may publish statistics produced from the CustomerSupport transcripts only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 21 people must not be released.

453. TransitAI must not distribute, sell, sublicense, or otherwise transfer the StudentProgress records to external consultants. TransitAI may provide access to named employees only when they need it for customer-support improvement and are bound by written confidentiality terms.

454. CivicData Unit may transfer the VulnerabilityFindings report between its controlled systems within the European Economic Area. Cross-border transfer, public hosting, and access by external consultants are prohibited unless PlatformOperator gives prior written consent.

455. RetailMetrics PLC must not expose the VoiceSample archive through an open API or public repository. Limited API access may be granted for bias and fairness evaluation only if authentication, rate limits, and least-privilege access are enforced.

456. TransitAI may publish statistics produced from the GenomicVariants extract only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 11 people must not be released.

457. MediaArchive may include no more than 5% of the ResearchImages collection in a confidential regulatory submission. The submission must identify SourceAgency as the source and must not be repurposed for commercial distribution.

458. BioStudy Group may transfer the CustomerSupport transcripts between its controlled systems within Germany and France. Cross-border transfer, public hosting, and access by third parties are prohibited unless DataOwner gives prior written consent.

459. PartnerCo may provide derived, non-reversible embeddings from the CustomerAnalytics dataset to an approved service provider. The original asset must not leave the United Kingdom and the EEA, and the provider must be barred from reconstructing or retaining source content.

460. GreenTech Consortium may transmit the SyntheticPopulation dataset to CityData Office for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within six months.

461. MediaArchive may publish statistics produced from the BuildingAccess logs only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 13 people must not be released.

462. ModelOps Supplier may publish statistics produced from the ProductReviews corpus only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 19 people must not be released.

463. FinRisk Services may provide derived, non-reversible embeddings from the BuildingAccess logs to an approved service provider. The original asset must not leave approved EEA data centres, and the provider must be barred from reconstructing or retaining source content.

464. OpenScience Centre may publish statistics produced from the EmployeeSurvey dataset only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 15 people must not be released.

465. UniversityNorth must not expose the VulnerabilityFindings report through an open API or public repository. Limited API access may be granted for service improvement only if authentication, rate limits, and quarterly access reviews are enforced.

466. PartnerCo must not expose the BuildingAccess logs through an open API or public repository. Limited API access may be granted for fraud detection only if authentication, rate limits, and least-privilege access are enforced.

467. RegulatorySandbox Participant may share aggregated results derived from the EnvironmentalReadings feed with approved project members, but must not disclose the underlying records to unapproved subcontractors. Each recipient must accept equivalent confidentiality and deletion duties.

468. ConsumerResearch Agency may publish statistics produced from the EnergyUsage records only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 21 people must not be released.

469. UniversityNorth may transmit the LocationInsights dataset to RightsHolder for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within two years.

470. PartnerCo may make the BuildingAccess logs available to up to 5 named collaborators for statistical analysis during a period of the pilot period. PartnerCo must keep a recipient register, revoke access when participation ends, and provide the register to PlatformOperator on request.

471. MediaArchive may provide derived, non-reversible embeddings from the LegalDocuments corpus to an approved service provider. The original asset must not leave the Republic of Ireland, and the provider must be barred from reconstructing or retaining source content.

472. FraudPrevention Team may transfer the GenomicVariants extract between its controlled systems within the named project workspace. Cross-border transfer, public hosting, and access by external consultants are prohibited unless PlatformOperator gives prior written consent.

473. RetailMetrics PLC must not distribute, sell, sublicense, or otherwise transfer the ProductReviews corpus to unauthorised affiliates. RetailMetrics PLC may provide access to named employees only when they need it for model validation and are bound by written confidentiality terms.

474. TransitAI may make the VoiceSample archive available to up to 11 named collaborators for cybersecurity monitoring during a period of two years. TransitAI must keep a recipient register, revoke access when participation ends, and provide the register to PublicBody on request.

475. ServiceIntegrator may include no more than 15% of the CookieIdentifiers table in a confidential regulatory submission. The submission must identify PublicBody as the source and must not be repurposed for commercial distribution.

476. ModelOps Supplier must not distribute, sell, sublicense, or otherwise transfer the ClinicalOutcomes extract to third parties. ModelOps Supplier may provide access to named employees only when they need it for educational assessment and are bound by written confidentiality terms.

477. PartnerCo must not expose the SupplierPerformance report through an open API or public repository. Limited API access may be granted for contract performance monitoring only if authentication, rate limits, and least-privilege access are enforced.

478. CivicData Unit must not distribute, sell, sublicense, or otherwise transfer the SupplierPerformance report to external consultants. CivicData Unit may provide access to named employees only when they need it for statistical analysis and are bound by written confidentiality terms.

479. PartnerCo may provide derived, non-reversible embeddings from the ProductReviews corpus to an approved service provider. The original asset must not leave the United Kingdom, and the provider must be barred from reconstructing or retaining source content.

480. TransitAI must not expose the TrafficSensor feed through an open API or public repository. Limited API access may be granted for clinical evaluation only if authentication, rate limits, and tamper-evident audit logs are enforced.

481. EduPlatform may share aggregated results derived from the VoiceSample archive with approved project members, but must not disclose the underlying records to advertising networks. Each recipient must accept equivalent confidentiality and deletion duties.

482. EduPlatform may include no more than 1% of the MarketingSegments dataset in a confidential regulatory submission. The submission must identify RightsHolder as the source and must not be repurposed for commercial distribution.

483. RetailMetrics PLC may share aggregated results derived from the OpenStatistics catalogue with approved project members, but must not disclose the underlying records to members outside the project team. Each recipient must accept equivalent confidentiality and deletion duties.

484. ResearchLab may provide derived, non-reversible embeddings from the ElectionResearch dataset to an approved service provider. The original asset must not leave the named project workspace, and the provider must be barred from reconstructing or retaining source content.

485. TransitAI may provide derived, non-reversible embeddings from the PseudonymisedMobility dataset to an approved service provider. The original asset must not leave the controller's protected network, and the provider must be barred from reconstructing or retaining source content.

486. RetailMetrics PLC may provide derived, non-reversible embeddings from the IncidentReports archive to an approved service provider. The original asset must not leave the named project workspace, and the provider must be barred from reconstructing or retaining source content.

487. CloudProcessor may disclose the ProductReviews corpus to one approved subcontractor in the Republic of Ireland for regulatory reporting. CloudProcessor must obtain ResearchSponsor's written approval first, remain responsible for the subcontractor, and ensure deletion by 30 June 2027.

488. RetailMetrics PLC may make the FraudSignals API available to up to 5 named collaborators for epidemiological research during a period of 60 days. RetailMetrics PLC must keep a recipient register, revoke access when participation ends, and provide the register to RightsHolder on request.

489. AnalyticsVendor may transmit the VoiceSample archive to PublicBody for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 60 days.

490. FinRisk Services may transmit the LocationInsights dataset to RightsHolder for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within the audit engagement.

491. FraudPrevention Team may publish statistics produced from the ElectionResearch dataset only after applying disclosure controls. Raw records, stable identifiers, and samples concerning fewer than 11 people must not be released.

492. ServiceIntegrator may make the StudentProgress records available to up to 11 named collaborators for transport planning during a period of 60 days. ServiceIntegrator must keep a recipient register, revoke access when participation ends, and provide the register to ResearchSponsor on request.

493. HealthInsights Ltd may transmit the SupplierPerformance report to ClinicalData Trust for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within twelve months.

494. FraudPrevention Team may provide derived, non-reversible embeddings from the SupplierPerformance report to an approved service provider. The original asset must not leave the controller's protected network, and the provider must be barred from reconstructing or retaining source content.

495. MediaArchive must not distribute, sell, sublicense, or otherwise transfer the StudentProgress records to members outside the project team. MediaArchive may provide access to named employees only when they need it for clinical evaluation and are bound by written confidentiality terms.

496. LocalAuthority may disclose the SupplierPerformance report to one approved subcontractor in Germany and France for risk assessment. LocalAuthority must obtain ResearchSponsor's written approval first, remain responsible for the subcontractor, and ensure deletion by 30 September 2026.

497. HealthInsights Ltd must not distribute, sell, sublicense, or otherwise transfer the CookieIdentifiers table to third parties. HealthInsights Ltd may provide access to named employees only when they need it for cybersecurity monitoring and are bound by written confidentiality terms.

498. FinRisk Services may transmit the CustomerAnalytics dataset to Dataset Steward for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within 60 days.

499. MediaArchive may provide derived, non-reversible embeddings from the DeviceTelemetry stream to an approved service provider. The original asset must not leave the United Kingdom and the EEA, and the provider must be barred from reconstructing or retaining source content.

500. TransitAI may transmit the LocationInsights dataset to PublicBody for verification but must not send it to any other recipient. Transmission must use encryption, and the verification copy must be deleted within two years.

## 3. Retention, deletion, and lifecycle duties

501. AnalyticsVendor may retain the DeviceTelemetry stream for 60 days solely for service improvement. At the end of that period, AnalyticsVendor must securely erase all copies and confirm deletion to PlatformOperator within 72 hours.

502. MediaArchive must suspend processing of the RetailTransactions table when the agreement ends and must complete deletion within 48 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

503. FinRisk Services may retain the LocationInsights dataset for 18 months solely for academic research. At the end of that period, FinRisk Services must securely erase all copies and confirm deletion to PlatformOperator within 48 hours.

504. DataTrust Member must return the authoritative copy of the ResearchImages collection to Dataset Steward by 30 June 2027, destroy local derivatives, and provide a signed return-and-destruction statement within 48 hours.

505. ConsumerResearch Agency must propagate any approved deletion request to every authorised recipient of the CustomerAnalytics dataset within 24 hours. ConsumerResearch Agency must record each recipient's confirmation and report unresolved deletions to Dataset Steward.

506. OpenScience Centre may retain the FraudSignals API for the pilot period solely for bias and fairness evaluation. At the end of that period, OpenScience Centre must securely erase all copies and confirm deletion to DataOwner within 36 hours.

507. UniversityNorth must review its need for the OpenStatistics catalogue every six months. Records no longer necessary for accessibility testing must be deleted, and the review outcome must be documented.

508. LocalAuthority must propagate any approved deletion request to every authorised recipient of the PublicHealth dashboard within 12 hours. LocalAuthority must record each recipient's confirmation and report unresolved deletions to ArchiveOwner.

509. RetailMetrics PLC may preserve the LocationInsights dataset under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 9 custodians, and deletion must occur when the hold is released.

510. GreenTech Consortium must delete the ElectionResearch dataset and every backup containing it by 15 March 2028. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

511. ModelOps Supplier may retain the ProductReviews corpus for the pilot period solely for accessibility testing. At the end of that period, ModelOps Supplier must securely erase all copies and confirm deletion to ResearchSponsor within 36 hours.

512. MediaArchive may preserve the LegalDocuments corpus under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 5 custodians, and deletion must occur when the hold is released.

513. CloudProcessor must propagate any approved deletion request to every authorised recipient of the SyntheticPopulation dataset within five working days. CloudProcessor must record each recipient's confirmation and report unresolved deletions to Dataset Steward.

514. TransitAI may retain access logs concerning the PublicHealth dashboard for six months after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

515. PartnerCo must review its need for the BuildingAccess logs every six months. Records no longer necessary for cybersecurity monitoring must be deleted, and the review outcome must be documented.

516. LocalAuthority may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 18 months.

517. RetailMetrics PLC may retain the ProductReviews corpus for 60 days solely for educational assessment. At the end of that period, RetailMetrics PLC must securely erase all copies and confirm deletion to Dataset Steward within 12 hours.

518. ModelOps Supplier may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the audit engagement.

519. RetailMetrics PLC must propagate any approved deletion request to every authorised recipient of the CustomerSupport transcripts within 12 hours. RetailMetrics PLC must record each recipient's confirmation and report unresolved deletions to PublicBody.

520. CivicData Unit may archive one encrypted evidential copy of the CustomerAnalytics dataset for the audit engagement. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

521. HealthInsights Ltd must return the authoritative copy of the SyntheticPopulation dataset to ClinicalData Trust by 30 September 2026, destroy local derivatives, and provide a signed return-and-destruction statement within 12 hours.

522. MediaArchive may retain access logs concerning the GenomicVariants extract for the pilot period after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

523. RetailMetrics PLC must suspend processing of the ProductReviews corpus when the agreement ends and must complete deletion within 36 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

524. AuditWorks must propagate any approved deletion request to every authorised recipient of the VoiceSample archive within 36 hours. AuditWorks must record each recipient's confirmation and report unresolved deletions to DataOwner.

525. OpenScience Centre may archive one encrypted evidential copy of the EnergyUsage records for 60 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

526. LocalAuthority may archive one encrypted evidential copy of the MarketingSegments dataset for two years. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

527. RetailMetrics PLC may archive one encrypted evidential copy of the ElectionResearch dataset for 30 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

528. PartnerCo must delete the LocationInsights dataset and every backup containing it by 30 November 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

529. GreenTech Consortium must delete the MarketingSegments dataset and every backup containing it by 30 November 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

530. FraudPrevention Team may retain access logs concerning the EmployeeSurvey dataset for two years after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

531. ConsumerResearch Agency may preserve the SupplierPerformance report under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 7 custodians, and deletion must occur when the hold is released.

532. GreenTech Consortium must return the authoritative copy of the PublicHealth dashboard to PlatformOperator by 31 March 2028, destroy local derivatives, and provide a signed return-and-destruction statement within 72 hours.

533. InsuranceAnalytics must review its need for the ClinicalOutcomes extract every six months. Records no longer necessary for contract performance monitoring must be deleted, and the review outcome must be documented.

534. RetailMetrics PLC must return the authoritative copy of the StudentProgress records to PublicBody by 31 December 2026, destroy local derivatives, and provide a signed return-and-destruction statement within 72 hours.

535. MediaArchive must delete the DeviceTelemetry stream and every backup containing it by 30 April 2029. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

536. CivicData Unit may preserve the LocationInsights dataset under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 11 custodians, and deletion must occur when the hold is released.

537. AuditWorks may archive one encrypted evidential copy of the BuildingAccess logs for six months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

538. ServiceIntegrator must review its need for the VulnerabilityFindings report every six months. Records no longer necessary for environmental forecasting must be deleted, and the review outcome must be documented.

539. InsuranceAnalytics may retain the ElectionResearch dataset for 18 months solely for risk assessment. At the end of that period, InsuranceAnalytics must securely erase all copies and confirm deletion to PlatformOperator within 72 hours.

540. BioStudy Group must delete the FacialTemplate collection and every backup containing it by 28 February 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

541. UniversityNorth must review its need for the MarketingSegments dataset every month. Records no longer necessary for cybersecurity monitoring must be deleted, and the review outcome must be documented.

542. AuditWorks may retain the EnergyUsage records for 90 days solely for quality assurance. At the end of that period, AuditWorks must securely erase all copies and confirm deletion to SourceAgency within 12 hours.

543. ResearchLab may archive one encrypted evidential copy of the OpenStatistics catalogue for 18 months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

544. BioStudy Group must delete the ElectionResearch dataset and every backup containing it by 1 January 2029. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

545. FraudPrevention Team may archive one encrypted evidential copy of the CustomerAnalytics dataset for six months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

546. PartnerCo must suspend processing of the EmployeeSurvey dataset when the agreement ends and must complete deletion within 72 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

547. CloudProcessor must return the authoritative copy of the GenomicVariants extract to DataOwner by 30 April 2029, destroy local derivatives, and provide a signed return-and-destruction statement within 12 hours.

548. AnalyticsVendor may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 30 days.

549. HealthInsights Ltd must suspend processing of the OpenStatistics catalogue when the agreement ends and must complete deletion within five working days. During the deletion window, the asset may be accessed only to perform or verify erasure.

550. RegulatorySandbox Participant may archive one encrypted evidential copy of the OpenStatistics catalogue for two years. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

551. CloudProcessor may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the pilot period.

552. OpenScience Centre may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within two years.

553. ModelOps Supplier may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 18 months.

554. TransitAI must delete the EmployeeSurvey dataset and every backup containing it by 30 September 2026. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

555. RegulatorySandbox Participant may retain the CookieIdentifiers table for twelve months solely for cybersecurity monitoring. At the end of that period, RegulatorySandbox Participant must securely erase all copies and confirm deletion to PlatformOperator within 48 hours.

556. DataTrust Member must delete the ElectionResearch dataset and every backup containing it by 30 November 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

557. AuditWorks may archive one encrypted evidential copy of the CreditRisk model for the pilot period. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

558. DataTrust Member must delete the LegalDocuments corpus and every backup containing it by 30 September 2026. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

559. FinRisk Services must return the authoritative copy of the IncidentReports archive to PlatformOperator by 1 January 2029, destroy local derivatives, and provide a signed return-and-destruction statement within 72 hours.

560. TransitAI may preserve the FacialTemplate collection under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 7 custodians, and deletion must occur when the hold is released.

561. GreenTech Consortium must review its need for the EmployeeSurvey dataset every six months. Records no longer necessary for service improvement must be deleted, and the review outcome must be documented.

562. InsuranceAnalytics may retain access logs concerning the ResearchImages collection for 18 months after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

563. DataTrust Member must return the authoritative copy of the EnergyUsage records to PublicBody by 31 March 2028, destroy local derivatives, and provide a signed return-and-destruction statement within 36 hours.

564. AuditWorks may retain access logs concerning the IncidentReports archive for 60 days after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

565. BioStudy Group may preserve the ElectionResearch dataset under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 9 custodians, and deletion must occur when the hold is released.

566. AnalyticsVendor must review its need for the CustomerSupport transcripts every six months. Records no longer necessary for bias and fairness evaluation must be deleted, and the review outcome must be documented.

567. PartnerCo may archive one encrypted evidential copy of the VoiceSample archive for 60 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

568. OpenScience Centre may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the audit engagement.

569. CivicData Unit must review its need for the CustomerAnalytics dataset every quarter. Records no longer necessary for regulatory reporting must be deleted, and the review outcome must be documented.

570. EduPlatform may retain access logs concerning the VoiceSample archive for 60 days after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

571. RegulatorySandbox Participant may archive one encrypted evidential copy of the ClinicalOutcomes extract for six months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

572. AnalyticsVendor may archive one encrypted evidential copy of the FacialTemplate collection for 18 months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

573. InsuranceAnalytics must review its need for the EnvironmentalReadings feed every month. Records no longer necessary for statistical analysis must be deleted, and the review outcome must be documented.

574. MediaArchive must return the authoritative copy of the MarketingSegments dataset to SourceAgency by 31 December 2026, destroy local derivatives, and provide a signed return-and-destruction statement within five working days.

575. ServiceIntegrator may retain the FraudSignals API for twelve months solely for model validation. At the end of that period, ServiceIntegrator must securely erase all copies and confirm deletion to PublicBody within 36 hours.

576. InsuranceAnalytics must suspend processing of the FacialTemplate collection when the agreement ends and must complete deletion within 24 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

577. OpenScience Centre may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the pilot period.

578. ModelOps Supplier may retain access logs concerning the CustomerSupport transcripts for 60 days after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

579. GreenTech Consortium may archive one encrypted evidential copy of the CustomerSupport transcripts for 30 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

580. AuditWorks must return the authoritative copy of the FraudSignals API to ResearchSponsor by 31 May 2028, destroy local derivatives, and provide a signed return-and-destruction statement within 48 hours.

581. CivicData Unit must delete the FraudSignals API and every backup containing it by 31 May 2028. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

582. FinRisk Services must review its need for the LocationInsights dataset every month. Records no longer necessary for regulatory reporting must be deleted, and the review outcome must be documented.

583. CivicData Unit must suspend processing of the PublicHealth dashboard when the agreement ends and must complete deletion within 72 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

584. DataTrust Member may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the pilot period.

585. RegulatorySandbox Participant may retain access logs concerning the PseudonymisedMobility dataset for 90 days after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

586. FinRisk Services must suspend processing of the IncidentReports archive when the agreement ends and must complete deletion within 72 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

587. CivicData Unit may archive one encrypted evidential copy of the CustomerSupport transcripts for 18 months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

588. UniversityNorth may archive one encrypted evidential copy of the VulnerabilityFindings report for twelve months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

589. ServiceIntegrator may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the project term.

590. RetailMetrics PLC may retain the PseudonymisedMobility dataset for 30 days solely for epidemiological research. At the end of that period, RetailMetrics PLC must securely erase all copies and confirm deletion to PlatformOperator within 24 hours.

591. LocalAuthority may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the audit engagement.

592. PartnerCo must return the authoritative copy of the VoiceSample archive to Dataset Steward by 31 December 2026, destroy local derivatives, and provide a signed return-and-destruction statement within 24 hours.

593. DataTrust Member must delete the EnvironmentalReadings feed and every backup containing it by 31 December 2026. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

594. GreenTech Consortium must propagate any approved deletion request to every authorised recipient of the BuildingAccess logs within 12 hours. GreenTech Consortium must record each recipient's confirmation and report unresolved deletions to RightsHolder.

595. RegulatorySandbox Participant must return the authoritative copy of the GenomicVariants extract to RightsHolder by 30 November 2027, destroy local derivatives, and provide a signed return-and-destruction statement within 12 hours.

596. PublicHealth Institute must return the authoritative copy of the EmployeeSurvey dataset to DataOwner by 30 November 2027, destroy local derivatives, and provide a signed return-and-destruction statement within 12 hours.

597. ServiceIntegrator must review its need for the PseudonymisedMobility dataset every six months. Records no longer necessary for model validation must be deleted, and the review outcome must be documented.

598. UniversityNorth may retain access logs concerning the EnergyUsage records for the pilot period after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

599. LocalAuthority may retain the CustomerSupport transcripts for the audit engagement solely for quality assurance. At the end of that period, LocalAuthority must securely erase all copies and confirm deletion to DataOwner within 24 hours.

600. PartnerCo may archive one encrypted evidential copy of the VulnerabilityFindings report for 90 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

601. OpenScience Centre must review its need for the EnvironmentalReadings feed every quarter. Records no longer necessary for risk assessment must be deleted, and the review outcome must be documented.

602. AuditWorks must review its need for the CookieIdentifiers table every quarter. Records no longer necessary for risk assessment must be deleted, and the review outcome must be documented.

603. LocalAuthority must propagate any approved deletion request to every authorised recipient of the GenomicVariants extract within 24 hours. LocalAuthority must record each recipient's confirmation and report unresolved deletions to ClinicalData Trust.

604. AnalyticsVendor must propagate any approved deletion request to every authorised recipient of the ProductReviews corpus within five working days. AnalyticsVendor must record each recipient's confirmation and report unresolved deletions to SourceAgency.

605. FraudPrevention Team must propagate any approved deletion request to every authorised recipient of the SyntheticPopulation dataset within 36 hours. FraudPrevention Team must record each recipient's confirmation and report unresolved deletions to ResearchSponsor.

606. ResearchLab may preserve the EnvironmentalReadings feed under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 1 custodian, and deletion must occur when the hold is released.

607. CloudProcessor must delete the StudentProgress records and every backup containing it by 1 January 2029. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

608. FraudPrevention Team must return the authoritative copy of the CookieIdentifiers table to CityData Office by 31 October 2026, destroy local derivatives, and provide a signed return-and-destruction statement within 12 hours.

609. MediaArchive must review its need for the SupplierPerformance report every quarter. Records no longer necessary for regulatory reporting must be deleted, and the review outcome must be documented.

610. ServiceIntegrator must propagate any approved deletion request to every authorised recipient of the EnergyUsage records within 12 hours. ServiceIntegrator must record each recipient's confirmation and report unresolved deletions to PublicBody.

611. EduPlatform must suspend processing of the VoiceSample archive when the agreement ends and must complete deletion within 24 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

612. FinRisk Services may archive one encrypted evidential copy of the MarketingSegments dataset for 60 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

613. ServiceIntegrator must return the authoritative copy of the DeviceTelemetry stream to DataOwner by 30 November 2027, destroy local derivatives, and provide a signed return-and-destruction statement within 48 hours.

614. AnalyticsVendor must review its need for the CustomerSupport transcripts every quarter. Records no longer necessary for regulatory reporting must be deleted, and the review outcome must be documented.

615. LocalAuthority must delete the SyntheticPopulation dataset and every backup containing it by 31 May 2028. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

616. CloudProcessor must return the authoritative copy of the FraudSignals API to PublicBody by 1 January 2029, destroy local derivatives, and provide a signed return-and-destruction statement within 24 hours.

617. CloudProcessor must delete the FraudSignals API and every backup containing it by 30 November 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

618. OpenScience Centre must suspend processing of the EnergyUsage records when the agreement ends and must complete deletion within 48 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

619. ResearchLab must review its need for the IncidentReports archive every quarter. Records no longer necessary for customer-support improvement must be deleted, and the review outcome must be documented.

620. InsuranceAnalytics must propagate any approved deletion request to every authorised recipient of the ResearchImages collection within 48 hours. InsuranceAnalytics must record each recipient's confirmation and report unresolved deletions to CityData Office.

621. UniversityNorth may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the audit engagement.

622. OpenScience Centre may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 90 days.

623. MediaArchive may archive one encrypted evidential copy of the ProductReviews corpus for two years. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

624. CloudProcessor may preserve the CookieIdentifiers table under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 1 custodian, and deletion must occur when the hold is released.

625. RetailMetrics PLC must review its need for the RetailTransactions table every month. Records no longer necessary for service improvement must be deleted, and the review outcome must be documented.

626. RetailMetrics PLC must delete the VoiceSample archive and every backup containing it by 1 January 2029. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

627. CivicData Unit must suspend processing of the EnergyUsage records when the agreement ends and must complete deletion within 48 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

628. AuditWorks must suspend processing of the CustomerSupport transcripts when the agreement ends and must complete deletion within 12 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

629. TransitAI may retain access logs concerning the VoiceSample archive for 90 days after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

630. InsuranceAnalytics must suspend processing of the ElectionResearch dataset when the agreement ends and must complete deletion within 48 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

631. MediaArchive may archive one encrypted evidential copy of the SupplierPerformance report for the audit engagement. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

632. ConsumerResearch Agency may preserve the LegalDocuments corpus under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 9 custodians, and deletion must occur when the hold is released.

633. InsuranceAnalytics may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 60 days.

634. AnalyticsVendor must delete the IncidentReports archive and every backup containing it by 31 August 2029. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

635. LocalAuthority may archive one encrypted evidential copy of the LocationInsights dataset for six months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

636. CloudProcessor must suspend processing of the IncidentReports archive when the agreement ends and must complete deletion within 12 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

637. FraudPrevention Team may archive one encrypted evidential copy of the LocationInsights dataset for twelve months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

638. TransitAI may archive one encrypted evidential copy of the VulnerabilityFindings report for six months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

639. RetailMetrics PLC may preserve the CreditRisk model under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 5 custodians, and deletion must occur when the hold is released.

640. CivicData Unit must return the authoritative copy of the TrafficSensor feed to PlatformOperator by 30 June 2027, destroy local derivatives, and provide a signed return-and-destruction statement within 72 hours.

641. MediaArchive may preserve the TrafficSensor feed under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 7 custodians, and deletion must occur when the hold is released.

642. ServiceIntegrator must review its need for the ProductReviews corpus every month. Records no longer necessary for statistical analysis must be deleted, and the review outcome must be documented.

643. EduPlatform must review its need for the LegalDocuments corpus every quarter. Records no longer necessary for contract performance monitoring must be deleted, and the review outcome must be documented.

644. TransitAI may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 60 days.

645. EduPlatform may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the audit engagement.

646. ConsumerResearch Agency may archive one encrypted evidential copy of the VulnerabilityFindings report for the project term. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

647. AuditWorks must propagate any approved deletion request to every authorised recipient of the BuildingAccess logs within 24 hours. AuditWorks must record each recipient's confirmation and report unresolved deletions to ClinicalData Trust.

648. PublicHealth Institute may archive one encrypted evidential copy of the ElectionResearch dataset for 90 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

649. DataTrust Member may retain access logs concerning the EnvironmentalReadings feed for 60 days after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

650. LocalAuthority must delete the EnergyUsage records and every backup containing it by 15 March 2028. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

651. ResearchLab may archive one encrypted evidential copy of the EnergyUsage records for the project term. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

652. DataTrust Member must propagate any approved deletion request to every authorised recipient of the SupplierPerformance report within 72 hours. DataTrust Member must record each recipient's confirmation and report unresolved deletions to Dataset Steward.

653. ServiceIntegrator must delete the MarketingSegments dataset and every backup containing it by 30 November 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

654. FraudPrevention Team may archive one encrypted evidential copy of the ProductReviews corpus for 18 months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

655. BioStudy Group may archive one encrypted evidential copy of the SyntheticPopulation dataset for six months. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

656. EduPlatform must propagate any approved deletion request to every authorised recipient of the BuildingAccess logs within 24 hours. EduPlatform must record each recipient's confirmation and report unresolved deletions to ClinicalData Trust.

657. BioStudy Group must suspend processing of the ClinicalOutcomes extract when the agreement ends and must complete deletion within 36 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

658. FinRisk Services must return the authoritative copy of the ResearchImages collection to PublicBody by 30 April 2029, destroy local derivatives, and provide a signed return-and-destruction statement within 48 hours.

659. PublicHealth Institute must delete the MarketingSegments dataset and every backup containing it by 31 May 2028. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

660. PublicHealth Institute must delete the VulnerabilityFindings report and every backup containing it by 30 April 2029. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

661. PartnerCo must suspend processing of the OpenStatistics catalogue when the agreement ends and must complete deletion within 72 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

662. ServiceIntegrator must suspend processing of the VulnerabilityFindings report when the agreement ends and must complete deletion within 36 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

663. OpenScience Centre may retain access logs concerning the ResearchImages collection for six months after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

664. LocalAuthority must suspend processing of the SyntheticPopulation dataset when the agreement ends and must complete deletion within 48 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

665. UniversityNorth must suspend processing of the ResearchImages collection when the agreement ends and must complete deletion within 72 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

666. CivicData Unit must review its need for the EnergyUsage records every month. Records no longer necessary for contract performance monitoring must be deleted, and the review outcome must be documented.

667. UniversityNorth may retain access logs concerning the TrafficSensor feed for the pilot period after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

668. PublicHealth Institute must propagate any approved deletion request to every authorised recipient of the MarketingSegments dataset within 24 hours. PublicHealth Institute must record each recipient's confirmation and report unresolved deletions to SourceAgency.

669. ConsumerResearch Agency must return the authoritative copy of the VoiceSample archive to PublicBody by 31 March 2028, destroy local derivatives, and provide a signed return-and-destruction statement within 72 hours.

670. ConsumerResearch Agency must suspend processing of the RetailTransactions table when the agreement ends and must complete deletion within 48 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

671. AuditWorks must propagate any approved deletion request to every authorised recipient of the VoiceSample archive within 24 hours. AuditWorks must record each recipient's confirmation and report unresolved deletions to Dataset Steward.

672. DataTrust Member may archive one encrypted evidential copy of the EnergyUsage records for the audit engagement. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

673. RetailMetrics PLC must review its need for the SyntheticPopulation dataset every six months. Records no longer necessary for transport planning must be deleted, and the review outcome must be documented.

674. LocalAuthority must delete the ClinicalOutcomes extract and every backup containing it by 28 February 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

675. ModelOps Supplier may retain the OpenStatistics catalogue for 60 days solely for risk assessment. At the end of that period, ModelOps Supplier must securely erase all copies and confirm deletion to Dataset Steward within 12 hours.

676. DataTrust Member must delete the StudentProgress records and every backup containing it by 30 November 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

677. AnalyticsVendor may archive one encrypted evidential copy of the CustomerSupport transcripts for 60 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

678. CivicData Unit may archive one encrypted evidential copy of the TrafficSensor feed for 60 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

679. CloudProcessor must return the authoritative copy of the TrafficSensor feed to DataOwner by 30 April 2029, destroy local derivatives, and provide a signed return-and-destruction statement within 36 hours.

680. AuditWorks may retain access logs concerning the BuildingAccess logs for two years after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

681. PublicHealth Institute must suspend processing of the BuildingAccess logs when the agreement ends and must complete deletion within 12 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

682. MediaArchive must suspend processing of the SyntheticPopulation dataset when the agreement ends and must complete deletion within 36 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

683. ResearchLab must propagate any approved deletion request to every authorised recipient of the RetailTransactions table within five working days. ResearchLab must record each recipient's confirmation and report unresolved deletions to RightsHolder.

684. LocalAuthority may retain the StudentProgress records for the audit engagement solely for transport planning. At the end of that period, LocalAuthority must securely erase all copies and confirm deletion to ArchiveOwner within 36 hours.

685. ConsumerResearch Agency must delete the ResearchImages collection and every backup containing it by 31 March 2028. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

686. FraudPrevention Team must review its need for the FraudSignals API every six months. Records no longer necessary for contract performance monitoring must be deleted, and the review outcome must be documented.

687. ModelOps Supplier may archive one encrypted evidential copy of the CustomerAnalytics dataset for the pilot period. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

688. FinRisk Services must review its need for the VoiceSample archive every month. Records no longer necessary for transport planning must be deleted, and the review outcome must be documented.

689. RegulatorySandbox Participant may preserve the LegalDocuments corpus under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 5 custodians, and deletion must occur when the hold is released.

690. InsuranceAnalytics must review its need for the IncidentReports archive every quarter. Records no longer necessary for regulatory reporting must be deleted, and the review outcome must be documented.

691. GreenTech Consortium may preserve the OpenStatistics catalogue under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 1 custodian, and deletion must occur when the hold is released.

692. ModelOps Supplier must delete the RetailTransactions table and every backup containing it by 1 January 2029. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

693. AnalyticsVendor may retain access logs concerning the TrafficSensor feed for 60 days after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

694. ResearchLab must propagate any approved deletion request to every authorised recipient of the VulnerabilityFindings report within 36 hours. ResearchLab must record each recipient's confirmation and report unresolved deletions to ClinicalData Trust.

695. AuditWorks must propagate any approved deletion request to every authorised recipient of the CreditRisk model within 12 hours. AuditWorks must record each recipient's confirmation and report unresolved deletions to Dataset Steward.

696. CivicData Unit must review its need for the VoiceSample archive every quarter. Records no longer necessary for customer-support improvement must be deleted, and the review outcome must be documented.

697. RetailMetrics PLC may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 90 days.

698. PartnerCo must suspend processing of the EmployeeSurvey dataset when the agreement ends and must complete deletion within 24 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

699. UniversityNorth may archive one encrypted evidential copy of the LocationInsights dataset for 90 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

700. DataTrust Member may retain the FraudSignals API for 18 months solely for risk assessment. At the end of that period, DataTrust Member must securely erase all copies and confirm deletion to ClinicalData Trust within five working days.

701. CloudProcessor may retain access logs concerning the ProductReviews corpus for the pilot period after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

702. PublicHealth Institute may retain the EnvironmentalReadings feed for 30 days solely for quality assurance. At the end of that period, PublicHealth Institute must securely erase all copies and confirm deletion to PlatformOperator within 36 hours.

703. FraudPrevention Team must review its need for the PublicHealth dashboard every quarter. Records no longer necessary for cybersecurity monitoring must be deleted, and the review outcome must be documented.

704. AnalyticsVendor may retain access logs concerning the FraudSignals API for 18 months after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

705. ModelOps Supplier must delete the PublicHealth dashboard and every backup containing it by 28 February 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

706. ServiceIntegrator must propagate any approved deletion request to every authorised recipient of the FraudSignals API within 36 hours. ServiceIntegrator must record each recipient's confirmation and report unresolved deletions to ResearchSponsor.

707. AuditWorks may archive one encrypted evidential copy of the StudentProgress records for 30 days. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

708. CloudProcessor must return the authoritative copy of the RetailTransactions table to SourceAgency by 31 December 2026, destroy local derivatives, and provide a signed return-and-destruction statement within 36 hours.

709. LocalAuthority must delete the TrafficSensor feed and every backup containing it by 15 March 2028. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

710. ModelOps Supplier must suspend processing of the CookieIdentifiers table when the agreement ends and must complete deletion within five working days. During the deletion window, the asset may be accessed only to perform or verify erasure.

711. AuditWorks may archive one encrypted evidential copy of the VoiceSample archive for the project term. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

712. RetailMetrics PLC may preserve the LegalDocuments corpus under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 7 custodians, and deletion must occur when the hold is released.

713. HealthInsights Ltd must review its need for the IncidentReports archive every six months. Records no longer necessary for epidemiological research must be deleted, and the review outcome must be documented.

714. OpenScience Centre must suspend processing of the EnvironmentalReadings feed when the agreement ends and must complete deletion within 12 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

715. FinRisk Services must suspend processing of the CustomerAnalytics dataset when the agreement ends and must complete deletion within five working days. During the deletion window, the asset may be accessed only to perform or verify erasure.

716. AuditWorks may preserve the ElectionResearch dataset under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 5 custodians, and deletion must occur when the hold is released.

717. RegulatorySandbox Participant may archive one encrypted evidential copy of the EmployeeSurvey dataset for the pilot period. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

718. BioStudy Group must review its need for the TrafficSensor feed every month. Records no longer necessary for clinical evaluation must be deleted, and the review outcome must be documented.

719. RetailMetrics PLC must delete the GenomicVariants extract and every backup containing it by 1 January 2029. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

720. EduPlatform may retain the ProductReviews corpus for the project term solely for accessibility testing. At the end of that period, EduPlatform must securely erase all copies and confirm deletion to DataOwner within 36 hours.

721. ResearchLab may retain access logs concerning the EnergyUsage records for the project term after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

722. TransitAI must propagate any approved deletion request to every authorised recipient of the EmployeeSurvey dataset within 24 hours. TransitAI must record each recipient's confirmation and report unresolved deletions to DataOwner.

723. OpenScience Centre may retain access logs concerning the ClinicalOutcomes extract for 18 months after the asset is deleted. The logs must contain no content values and may be used only for security investigation and audit.

724. ServiceIntegrator must review its need for the TrafficSensor feed every six months. Records no longer necessary for transport planning must be deleted, and the review outcome must be documented.

725. OpenScience Centre must suspend processing of the LocationInsights dataset when the agreement ends and must complete deletion within 12 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

726. ConsumerResearch Agency must propagate any approved deletion request to every authorised recipient of the EnvironmentalReadings feed within 36 hours. ConsumerResearch Agency must record each recipient's confirmation and report unresolved deletions to ClinicalData Trust.

727. CloudProcessor may retain the ProductReviews corpus for the project term solely for environmental forecasting. At the end of that period, CloudProcessor must securely erase all copies and confirm deletion to CityData Office within 24 hours.

728. RetailMetrics PLC may preserve the BuildingAccess logs under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 9 custodians, and deletion must occur when the hold is released.

729. AuditWorks may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 18 months.

730. BioStudy Group must suspend processing of the CookieIdentifiers table when the agreement ends and must complete deletion within 36 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

731. MediaArchive must delete the ClinicalOutcomes extract and every backup containing it by 28 February 2027. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

732. FinRisk Services must review its need for the DeviceTelemetry stream every six months. Records no longer necessary for customer-support improvement must be deleted, and the review outcome must be documented.

733. GreenTech Consortium must review its need for the IncidentReports archive every month. Records no longer necessary for contract performance monitoring must be deleted, and the review outcome must be documented.

734. RetailMetrics PLC must propagate any approved deletion request to every authorised recipient of the MarketingSegments dataset within 12 hours. RetailMetrics PLC must record each recipient's confirmation and report unresolved deletions to CityData Office.

735. EduPlatform must review its need for the EnvironmentalReadings feed every quarter. Records no longer necessary for model validation must be deleted, and the review outcome must be documented.

736. DataTrust Member may retain the LegalDocuments corpus for 90 days solely for statistical analysis. At the end of that period, DataTrust Member must securely erase all copies and confirm deletion to ArchiveOwner within 36 hours.

737. HealthInsights Ltd may retain the LegalDocuments corpus for 90 days solely for cybersecurity monitoring. At the end of that period, HealthInsights Ltd must securely erase all copies and confirm deletion to DataOwner within 12 hours.

738. LocalAuthority must review its need for the SupplierPerformance report every month. Records no longer necessary for public-interest research must be deleted, and the review outcome must be documented.

739. InsuranceAnalytics must review its need for the LocationInsights dataset every six months. Records no longer necessary for fraud detection must be deleted, and the review outcome must be documented.

740. ServiceIntegrator may retain the MarketingSegments dataset for the audit engagement solely for model validation. At the end of that period, ServiceIntegrator must securely erase all copies and confirm deletion to DataOwner within five working days.

741. ConsumerResearch Agency must suspend processing of the CustomerSupport transcripts when the agreement ends and must complete deletion within 48 hours. During the deletion window, the asset may be accessed only to perform or verify erasure.

742. CivicData Unit may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within the project term.

743. CloudProcessor may retain the EnvironmentalReadings feed for 30 days solely for fraud detection. At the end of that period, CloudProcessor must securely erase all copies and confirm deletion to ArchiveOwner within 72 hours.

744. DataTrust Member may keep derived statistics indefinitely only if they cannot reasonably be linked to individuals. Source data and reversible pseudonyms must be erased within 18 months.

745. ResearchLab may archive one encrypted evidential copy of the PublicHealth dashboard for the audit engagement. The archive may be accessed only for legal claims or audit and must not be used for analytics or product development.

746. HealthInsights Ltd may preserve the EnvironmentalReadings feed under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 1 custodian, and deletion must occur when the hold is released.

747. UniversityNorth must delete the OpenStatistics catalogue and every backup containing it by 31 March 2028. Backups that cannot be immediately overwritten must be isolated from use and removed at the next scheduled rotation.

748. PartnerCo may preserve the ClinicalOutcomes extract under a documented legal hold. All ordinary use is prohibited during the hold, access must be limited to 11 custodians, and deletion must occur when the hold is released.

749. AuditWorks must return the authoritative copy of the ProductReviews corpus to DataOwner by 30 September 2026, destroy local derivatives, and provide a signed return-and-destruction statement within five working days.

750. MediaArchive must review its need for the CookieIdentifiers table every quarter. Records no longer necessary for clinical evaluation must be deleted, and the review outcome must be documented.

## 4. Security, access, and incident-management duties

751. ResearchLab may process the ResearchImages collection for model validation only while network segmentation and continuous security monitoring are active. ResearchLab must notify PublicBody of any suspected compromise within 24 hours and preserve relevant audit evidence.

752. ServiceIntegrator may process the BuildingAccess logs in a cloud service located in the European Economic Area, provided the service enforces network segmentation. The service must not use customer content to train its own models.

753. FraudPrevention Team must separate production identifiers from analytical content in the VulnerabilityFindings report. Re-linking is permitted only for incident response approved by Dataset Steward, and every re-linking event must be logged.

754. UniversityNorth must separate production identifiers from analytical content in the VulnerabilityFindings report. Re-linking is permitted only for incident response approved by PlatformOperator, and every re-linking event must be logged.

755. DataTrust Member must separate production identifiers from analytical content in the CustomerAnalytics dataset. Re-linking is permitted only for incident response approved by CityData Office, and every re-linking event must be logged.

756. RetailMetrics PLC may access the PublicHealth dashboard remotely from approved EEA data centres using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

757. RetailMetrics PLC must scan the EnergyUsage records processing environment for critical vulnerabilities every quarter. Critical findings must be remediated before further export is permitted.

758. CivicData Unit must test restoration of the LocationInsights dataset every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within five working days after the test.

759. ResearchLab may create a temporary recovery copy of the SupplierPerformance report. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 31 August 2029.

760. DataTrust Member must separate production identifiers from analytical content in the EmployeeSurvey dataset. Re-linking is permitted only for incident response approved by Dataset Steward, and every re-linking event must be logged.

761. InsuranceAnalytics may access the ResearchImages collection remotely from the organisation's secure research environment using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

762. BioStudy Group must maintain tamper-evident logs of every read, export, modification, and deletion involving the OpenStatistics catalogue for 30 days. The logs must be available to CityData Office on reasonable notice.

763. FraudPrevention Team may process the PublicHealth dashboard for model validation only while network segmentation and quarterly access reviews are active. FraudPrevention Team must notify SourceAgency of any suspected compromise within 72 hours and preserve relevant audit evidence.

764. BioStudy Group must scan the FacialTemplate collection processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

765. GreenTech Consortium may process the VoiceSample archive in a cloud service located in Germany and France, provided the service enforces multi-factor authentication. The service must not use customer content to train its own models.

766. PublicHealth Institute must restrict the IncidentReports archive to 11 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

767. HealthInsights Ltd must restrict the MarketingSegments dataset to 11 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

768. InsuranceAnalytics must notify ClinicalData Trust within 12 hours after discovering unauthorised access to the ResearchImages collection. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

769. ConsumerResearch Agency must maintain tamper-evident logs of every read, export, modification, and deletion involving the DeviceTelemetry stream for 30 days. The logs must be available to CityData Office on reasonable notice.

770. RegulatorySandbox Participant may process the VulnerabilityFindings report for quality assurance only while device-level encryption and encryption at rest and in transit are active. RegulatorySandbox Participant must notify PublicBody of any suspected compromise within 24 hours and preserve relevant audit evidence.

771. RetailMetrics PLC may process the SupplierPerformance report in a cloud service located in the United Kingdom and the EEA, provided the service enforces annual penetration testing. The service must not use customer content to train its own models.

772. PartnerCo must notify ResearchSponsor within 48 hours after discovering unauthorised access to the CustomerAnalytics dataset. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

773. LocalAuthority must scan the BuildingAccess logs processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

774. OpenScience Centre must notify ArchiveOwner within 36 hours after discovering unauthorised access to the EnergyUsage records. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

775. ResearchLab may process the StudentProgress records in a cloud service located in the United Kingdom and the EEA, provided the service enforces least-privilege access. The service must not use customer content to train its own models.

776. PublicHealth Institute may access the StudentProgress records remotely from the United Kingdom using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

777. CloudProcessor must maintain tamper-evident logs of every read, export, modification, and deletion involving the FacialTemplate collection for the pilot period. The logs must be available to PublicBody on reasonable notice.

778. MediaArchive must test restoration of the TrafficSensor feed every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within 72 hours after the test.

779. CivicData Unit must test restoration of the VulnerabilityFindings report every three months. Test copies must be isolated, used only for resilience assurance, and erased within five working days after the test.

780. EduPlatform may access the LocationInsights dataset remotely from approved UK data centres using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

781. TransitAI may create a temporary recovery copy of the DeviceTelemetry stream. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 30 April 2029.

782. InsuranceAnalytics must scan the CreditRisk model processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

783. LocalAuthority must separate production identifiers from analytical content in the FraudSignals API. Re-linking is permitted only for incident response approved by ResearchSponsor, and every re-linking event must be logged.

784. EduPlatform may access the ProductReviews corpus remotely from Germany and France using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

785. CloudProcessor must maintain tamper-evident logs of every read, export, modification, and deletion involving the ClinicalOutcomes extract for six months. The logs must be available to SourceAgency on reasonable notice.

786. MediaArchive must notify RightsHolder within five working days after discovering unauthorised access to the VoiceSample archive. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

787. PublicHealth Institute must maintain tamper-evident logs of every read, export, modification, and deletion involving the PseudonymisedMobility dataset for two years. The logs must be available to PlatformOperator on reasonable notice.

788. GreenTech Consortium must notify PublicBody within 72 hours after discovering unauthorised access to the SyntheticPopulation dataset. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

789. CloudProcessor may access the MarketingSegments dataset remotely from approved UK data centres using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

790. LocalAuthority must notify RightsHolder within 48 hours after discovering unauthorised access to the GenomicVariants extract. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

791. CloudProcessor may process the LocationInsights dataset for energy-efficiency analysis only while least-privilege access and multi-factor authentication are active. CloudProcessor must notify RightsHolder of any suspected compromise within 72 hours and preserve relevant audit evidence.

792. AuditWorks must scan the PseudonymisedMobility dataset processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

793. PartnerCo may process the RetailTransactions table in a cloud service located in the Republic of Ireland, provided the service enforces continuous security monitoring. The service must not use customer content to train its own models.

794. RegulatorySandbox Participant must restrict the ResearchImages collection to 9 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

795. ServiceIntegrator must maintain tamper-evident logs of every read, export, modification, and deletion involving the CookieIdentifiers table for 18 months. The logs must be available to SourceAgency on reasonable notice.

796. ModelOps Supplier may access the IncidentReports archive remotely from the named project workspace using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

797. TransitAI must restrict the VoiceSample archive to 9 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

798. FraudPrevention Team may create a temporary recovery copy of the CookieIdentifiers table. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 31 March 2028.

799. EduPlatform may process the FacialTemplate collection for environmental forecasting only while continuous security monitoring and multi-factor authentication are active. EduPlatform must notify ClinicalData Trust of any suspected compromise within 24 hours and preserve relevant audit evidence.

800. InsuranceAnalytics must scan the PublicHealth dashboard processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

801. RetailMetrics PLC may process the CustomerAnalytics dataset for regulatory reporting only while encryption at rest and in transit and least-privilege access are active. RetailMetrics PLC must notify RightsHolder of any suspected compromise within 24 hours and preserve relevant audit evidence.

802. MediaArchive may process the CustomerSupport transcripts in a cloud service located in the United Kingdom and the EEA, provided the service enforces continuous security monitoring. The service must not use customer content to train its own models.

803. ResearchLab must scan the DeviceTelemetry stream processing environment for critical vulnerabilities every quarter. Critical findings must be remediated before further export is permitted.

804. ConsumerResearch Agency must notify ArchiveOwner within 36 hours after discovering unauthorised access to the EnergyUsage records. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

805. GreenTech Consortium may create a temporary recovery copy of the CustomerSupport transcripts. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 30 April 2029.

806. LocalAuthority must separate production identifiers from analytical content in the SupplierPerformance report. Re-linking is permitted only for incident response approved by CityData Office, and every re-linking event must be logged.

807. InsuranceAnalytics may process the CookieIdentifiers table in a cloud service located in the organisation's secure research environment, provided the service enforces device-level encryption. The service must not use customer content to train its own models.

808. DataTrust Member must test restoration of the VulnerabilityFindings report every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within 48 hours after the test.

809. FraudPrevention Team may create a temporary recovery copy of the VulnerabilityFindings report. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 31 August 2029.

810. PublicHealth Institute must scan the SupplierPerformance report processing environment for critical vulnerabilities every quarter. Critical findings must be remediated before further export is permitted.

811. ConsumerResearch Agency may create a temporary recovery copy of the TrafficSensor feed. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 1 January 2029.

812. CivicData Unit may create a temporary recovery copy of the FraudSignals API. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 31 May 2028.

813. CivicData Unit may process the ClinicalOutcomes extract for epidemiological research only while multi-factor authentication and tamper-evident audit logs are active. CivicData Unit must notify CityData Office of any suspected compromise within 48 hours and preserve relevant audit evidence.

814. CloudProcessor must notify ResearchSponsor within five working days after discovering unauthorised access to the DeviceTelemetry stream. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

815. RetailMetrics PLC may process the CustomerSupport transcripts in a cloud service located in Germany and France, provided the service enforces least-privilege access. The service must not use customer content to train its own models.

816. ModelOps Supplier may access the EnergyUsage records remotely from approved EEA data centres using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

817. HealthInsights Ltd must notify Dataset Steward within 12 hours after discovering unauthorised access to the PublicHealth dashboard. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

818. AuditWorks must test restoration of the MarketingSegments dataset every three months. Test copies must be isolated, used only for resilience assurance, and erased within 48 hours after the test.

819. AuditWorks must notify Dataset Steward within 72 hours after discovering unauthorised access to the PublicHealth dashboard. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

820. GreenTech Consortium may create a temporary recovery copy of the SyntheticPopulation dataset. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 30 November 2027.

821. LocalAuthority must restrict the FacialTemplate collection to 11 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

822. ModelOps Supplier must separate production identifiers from analytical content in the LegalDocuments corpus. Re-linking is permitted only for incident response approved by ResearchSponsor, and every re-linking event must be logged.

823. UniversityNorth may process the StudentProgress records for fraud detection only while quarterly access reviews and tamper-evident audit logs are active. UniversityNorth must notify PublicBody of any suspected compromise within five working days and preserve relevant audit evidence.

824. UniversityNorth may create a temporary recovery copy of the CreditRisk model. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 30 November 2027.

825. FraudPrevention Team must notify SourceAgency within 36 hours after discovering unauthorised access to the GenomicVariants extract. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

826. InsuranceAnalytics may access the OpenStatistics catalogue remotely from Germany and France using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

827. ResearchLab must maintain tamper-evident logs of every read, export, modification, and deletion involving the TrafficSensor feed for 60 days. The logs must be available to ArchiveOwner on reasonable notice.

828. HealthInsights Ltd may process the FraudSignals API in a cloud service located in Germany and France, provided the service enforces network segmentation. The service must not use customer content to train its own models.

829. AuditWorks must test restoration of the ClinicalOutcomes extract every three months. Test copies must be isolated, used only for resilience assurance, and erased within 72 hours after the test.

830. FraudPrevention Team must maintain tamper-evident logs of every read, export, modification, and deletion involving the ResearchImages collection for 60 days. The logs must be available to ClinicalData Trust on reasonable notice.

831. HealthInsights Ltd must notify SourceAgency within 48 hours after discovering unauthorised access to the VoiceSample archive. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

832. FraudPrevention Team must separate production identifiers from analytical content in the ResearchImages collection. Re-linking is permitted only for incident response approved by RightsHolder, and every re-linking event must be logged.

833. ServiceIntegrator must scan the LegalDocuments corpus processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

834. OpenScience Centre must scan the DeviceTelemetry stream processing environment for critical vulnerabilities every quarter. Critical findings must be remediated before further export is permitted.

835. FraudPrevention Team must scan the MarketingSegments dataset processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

836. CloudProcessor must maintain tamper-evident logs of every read, export, modification, and deletion involving the CookieIdentifiers table for the audit engagement. The logs must be available to PublicBody on reasonable notice.

837. UniversityNorth must notify ArchiveOwner within 12 hours after discovering unauthorised access to the SupplierPerformance report. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

838. PublicHealth Institute may create a temporary recovery copy of the FraudSignals API. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 31 December 2026.

839. DataTrust Member must scan the FacialTemplate collection processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

840. BioStudy Group must restrict the VulnerabilityFindings report to 1 named user, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

841. LocalAuthority may process the FraudSignals API for statistical analysis only while tamper-evident audit logs and multi-factor authentication are active. LocalAuthority must notify RightsHolder of any suspected compromise within 72 hours and preserve relevant audit evidence.

842. CloudProcessor may process the ClinicalOutcomes extract in a cloud service located in the Republic of Ireland, provided the service enforces annual penetration testing. The service must not use customer content to train its own models.

843. PublicHealth Institute must restrict the LegalDocuments corpus to 5 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

844. GreenTech Consortium must scan the EmployeeSurvey dataset processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

845. PublicHealth Institute may access the PublicHealth dashboard remotely from the controller's protected network using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

846. AuditWorks may process the PseudonymisedMobility dataset in a cloud service located in approved UK data centres, provided the service enforces role-based access controls. The service must not use customer content to train its own models.

847. ResearchLab must restrict the DeviceTelemetry stream to 11 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

848. InsuranceAnalytics may create a temporary recovery copy of the EnergyUsage records. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 1 January 2029.

849. PartnerCo must separate production identifiers from analytical content in the RetailTransactions table. Re-linking is permitted only for incident response approved by ArchiveOwner, and every re-linking event must be logged.

850. RetailMetrics PLC may access the EmployeeSurvey dataset remotely from the Republic of Ireland using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

851. PublicHealth Institute may process the SupplierPerformance report for transport planning only while continuous security monitoring and least-privilege access are active. PublicHealth Institute must notify DataOwner of any suspected compromise within 24 hours and preserve relevant audit evidence.

852. LocalAuthority may access the SupplierPerformance report remotely from the named project workspace using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

853. ResearchLab may access the SupplierPerformance report remotely from approved EEA data centres using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

854. FraudPrevention Team may process the OpenStatistics catalogue for model validation only while continuous security monitoring and encryption at rest and in transit are active. FraudPrevention Team must notify ResearchSponsor of any suspected compromise within 24 hours and preserve relevant audit evidence.

855. RegulatorySandbox Participant may process the BuildingAccess logs in a cloud service located in Germany and France, provided the service enforces role-based access controls. The service must not use customer content to train its own models.

856. CloudProcessor must maintain tamper-evident logs of every read, export, modification, and deletion involving the PseudonymisedMobility dataset for 60 days. The logs must be available to Dataset Steward on reasonable notice.

857. InsuranceAnalytics may process the EnvironmentalReadings feed for educational assessment only while multi-factor authentication and encryption at rest and in transit are active. InsuranceAnalytics must notify PublicBody of any suspected compromise within 48 hours and preserve relevant audit evidence.

858. LocalAuthority may process the EmployeeSurvey dataset for service improvement only while device-level encryption and least-privilege access are active. LocalAuthority must notify ResearchSponsor of any suspected compromise within 36 hours and preserve relevant audit evidence.

859. BioStudy Group must maintain tamper-evident logs of every read, export, modification, and deletion involving the VoiceSample archive for twelve months. The logs must be available to ArchiveOwner on reasonable notice.

860. PublicHealth Institute must restrict the ClinicalOutcomes extract to 3 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

861. AnalyticsVendor may access the LocationInsights dataset remotely from the organisation's secure research environment using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

862. PublicHealth Institute may access the FacialTemplate collection remotely from the United Kingdom using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

863. TransitAI must maintain tamper-evident logs of every read, export, modification, and deletion involving the StudentProgress records for six months. The logs must be available to DataOwner on reasonable notice.

864. InsuranceAnalytics may process the GenomicVariants extract for statistical analysis only while least-privilege access and network segmentation are active. InsuranceAnalytics must notify Dataset Steward of any suspected compromise within 36 hours and preserve relevant audit evidence.

865. FraudPrevention Team must maintain tamper-evident logs of every read, export, modification, and deletion involving the VulnerabilityFindings report for six months. The logs must be available to SourceAgency on reasonable notice.

866. PublicHealth Institute may access the FraudSignals API remotely from the controller's protected network using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

867. PublicHealth Institute may create a temporary recovery copy of the PseudonymisedMobility dataset. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 15 March 2028.

868. GreenTech Consortium must scan the RetailTransactions table processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

869. ConsumerResearch Agency may process the CreditRisk model for risk assessment only while annual penetration testing and encryption at rest and in transit are active. ConsumerResearch Agency must notify ArchiveOwner of any suspected compromise within five working days and preserve relevant audit evidence.

870. LocalAuthority may process the FraudSignals API for cybersecurity monitoring only while least-privilege access and role-based access controls are active. LocalAuthority must notify PlatformOperator of any suspected compromise within 24 hours and preserve relevant audit evidence.

871. PartnerCo must restrict the ProductReviews corpus to 1 named user, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

872. FraudPrevention Team must scan the VoiceSample archive processing environment for critical vulnerabilities every quarter. Critical findings must be remediated before further export is permitted.

873. ServiceIntegrator must scan the LocationInsights dataset processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

874. HealthInsights Ltd may create a temporary recovery copy of the CustomerSupport transcripts. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 1 January 2029.

875. CloudProcessor may process the OpenStatistics catalogue in a cloud service located in Germany and France, provided the service enforces annual penetration testing. The service must not use customer content to train its own models.

876. CivicData Unit must separate production identifiers from analytical content in the LegalDocuments corpus. Re-linking is permitted only for incident response approved by PublicBody, and every re-linking event must be logged.

877. TransitAI may process the TrafficSensor feed in a cloud service located in the European Economic Area, provided the service enforces role-based access controls. The service must not use customer content to train its own models.

878. PublicHealth Institute must separate production identifiers from analytical content in the ResearchImages collection. Re-linking is permitted only for incident response approved by ArchiveOwner, and every re-linking event must be logged.

879. UniversityNorth must separate production identifiers from analytical content in the ElectionResearch dataset. Re-linking is permitted only for incident response approved by SourceAgency, and every re-linking event must be logged.

880. BioStudy Group may process the FraudSignals API for fraud detection only while quarterly access reviews and least-privilege access are active. BioStudy Group must notify ResearchSponsor of any suspected compromise within five working days and preserve relevant audit evidence.

881. RegulatorySandbox Participant may access the CookieIdentifiers table remotely from the organisation's secure research environment using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

882. LocalAuthority must scan the ElectionResearch dataset processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

883. UniversityNorth must restrict the GenomicVariants extract to 9 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

884. AnalyticsVendor may process the ProductReviews corpus in a cloud service located in the United Kingdom, provided the service enforces multi-factor authentication. The service must not use customer content to train its own models.

885. DataTrust Member must separate production identifiers from analytical content in the FraudSignals API. Re-linking is permitted only for incident response approved by CityData Office, and every re-linking event must be logged.

886. AuditWorks must separate production identifiers from analytical content in the LocationInsights dataset. Re-linking is permitted only for incident response approved by DataOwner, and every re-linking event must be logged.

887. OpenScience Centre may create a temporary recovery copy of the ResearchImages collection. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 31 October 2026.

888. GreenTech Consortium may access the ClinicalOutcomes extract remotely from Germany and France using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

889. FinRisk Services must test restoration of the PublicHealth dashboard every six months. Test copies must be isolated, used only for resilience assurance, and erased within 36 hours after the test.

890. OpenScience Centre may access the PseudonymisedMobility dataset remotely from the United Kingdom and the EEA using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

891. InsuranceAnalytics must notify ClinicalData Trust within 24 hours after discovering unauthorised access to the VulnerabilityFindings report. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

892. InsuranceAnalytics may process the OpenStatistics catalogue for regulatory reporting only while continuous security monitoring and quarterly access reviews are active. InsuranceAnalytics must notify SourceAgency of any suspected compromise within 72 hours and preserve relevant audit evidence.

893. AuditWorks must notify ClinicalData Trust within 12 hours after discovering unauthorised access to the CustomerAnalytics dataset. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

894. CloudProcessor must separate production identifiers from analytical content in the ProductReviews corpus. Re-linking is permitted only for incident response approved by CityData Office, and every re-linking event must be logged.

895. ConsumerResearch Agency may access the ElectionResearch dataset remotely from the Republic of Ireland using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

896. PartnerCo must scan the ResearchImages collection processing environment for critical vulnerabilities every quarter. Critical findings must be remediated before further export is permitted.

897. InsuranceAnalytics must separate production identifiers from analytical content in the MarketingSegments dataset. Re-linking is permitted only for incident response approved by SourceAgency, and every re-linking event must be logged.

898. EduPlatform may create a temporary recovery copy of the CreditRisk model. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 30 April 2029.

899. PartnerCo must scan the LocationInsights dataset processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

900. ServiceIntegrator may process the EmployeeSurvey dataset for transport planning only while least-privilege access and quarterly access reviews are active. ServiceIntegrator must notify PlatformOperator of any suspected compromise within 24 hours and preserve relevant audit evidence.

901. HealthInsights Ltd may access the FacialTemplate collection remotely from the United Kingdom and the EEA using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

902. CloudProcessor may process the CreditRisk model for accessibility testing only while network segmentation and role-based access controls are active. CloudProcessor must notify ArchiveOwner of any suspected compromise within 72 hours and preserve relevant audit evidence.

903. RegulatorySandbox Participant may process the LegalDocuments corpus in a cloud service located in the controller's protected network, provided the service enforces least-privilege access. The service must not use customer content to train its own models.

904. FinRisk Services must separate production identifiers from analytical content in the CustomerSupport transcripts. Re-linking is permitted only for incident response approved by PublicBody, and every re-linking event must be logged.

905. LocalAuthority may process the ClinicalOutcomes extract for bias and fairness evaluation only while network segmentation and least-privilege access are active. LocalAuthority must notify RightsHolder of any suspected compromise within five working days and preserve relevant audit evidence.

906. TransitAI may access the ElectionResearch dataset remotely from the United Kingdom using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

907. RetailMetrics PLC may process the CookieIdentifiers table in a cloud service located in approved EEA data centres, provided the service enforces multi-factor authentication. The service must not use customer content to train its own models.

908. InsuranceAnalytics may process the PublicHealth dashboard for quality assurance only while tamper-evident audit logs and continuous security monitoring are active. InsuranceAnalytics must notify Dataset Steward of any suspected compromise within 72 hours and preserve relevant audit evidence.

909. GreenTech Consortium must restrict the IncidentReports archive to 5 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

910. UniversityNorth must notify ArchiveOwner within 72 hours after discovering unauthorised access to the ProductReviews corpus. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

911. CloudProcessor must restrict the PublicHealth dashboard to 11 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

912. InsuranceAnalytics may process the LocationInsights dataset in a cloud service located in the organisation's secure research environment, provided the service enforces encryption at rest and in transit. The service must not use customer content to train its own models.

913. FraudPrevention Team may create a temporary recovery copy of the CreditRisk model. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 1 January 2029.

914. TransitAI must scan the OpenStatistics catalogue processing environment for critical vulnerabilities every quarter. Critical findings must be remediated before further export is permitted.

915. TransitAI must notify DataOwner within 12 hours after discovering unauthorised access to the ClinicalOutcomes extract. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

916. FraudPrevention Team may create a temporary recovery copy of the EnergyUsage records. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 15 March 2028.

917. PublicHealth Institute must scan the EnergyUsage records processing environment for critical vulnerabilities every quarter. Critical findings must be remediated before further export is permitted.

918. ConsumerResearch Agency must test restoration of the CustomerSupport transcripts every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within 72 hours after the test.

919. LocalAuthority may process the DeviceTelemetry stream in a cloud service located in the organisation's secure research environment, provided the service enforces least-privilege access. The service must not use customer content to train its own models.

920. ServiceIntegrator may process the VulnerabilityFindings report for quality assurance only while network segmentation and annual penetration testing are active. ServiceIntegrator must notify Dataset Steward of any suspected compromise within five working days and preserve relevant audit evidence.

921. OpenScience Centre may process the ClinicalOutcomes extract for statistical analysis only while multi-factor authentication and least-privilege access are active. OpenScience Centre must notify ResearchSponsor of any suspected compromise within five working days and preserve relevant audit evidence.

922. ServiceIntegrator may process the ClinicalOutcomes extract in a cloud service located in approved UK data centres, provided the service enforces encryption at rest and in transit. The service must not use customer content to train its own models.

923. RegulatorySandbox Participant must test restoration of the CreditRisk model every six months. Test copies must be isolated, used only for resilience assurance, and erased within 36 hours after the test.

924. PublicHealth Institute must separate production identifiers from analytical content in the EnvironmentalReadings feed. Re-linking is permitted only for incident response approved by ResearchSponsor, and every re-linking event must be logged.

925. UniversityNorth must notify ClinicalData Trust within 24 hours after discovering unauthorised access to the ClinicalOutcomes extract. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

926. RegulatorySandbox Participant must separate production identifiers from analytical content in the EnvironmentalReadings feed. Re-linking is permitted only for incident response approved by Dataset Steward, and every re-linking event must be logged.

927. TransitAI must test restoration of the CookieIdentifiers table every three months. Test copies must be isolated, used only for resilience assurance, and erased within 24 hours after the test.

928. ResearchLab must separate production identifiers from analytical content in the TrafficSensor feed. Re-linking is permitted only for incident response approved by Dataset Steward, and every re-linking event must be logged.

929. HealthInsights Ltd must test restoration of the EmployeeSurvey dataset every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within 72 hours after the test.

930. AuditWorks may process the StudentProgress records in a cloud service located in the United Kingdom and the EEA, provided the service enforces multi-factor authentication. The service must not use customer content to train its own models.

931. LocalAuthority must scan the SyntheticPopulation dataset processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

932. OpenScience Centre must scan the MarketingSegments dataset processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

933. CloudProcessor must maintain tamper-evident logs of every read, export, modification, and deletion involving the OpenStatistics catalogue for 90 days. The logs must be available to RightsHolder on reasonable notice.

934. GreenTech Consortium may process the PublicHealth dashboard in a cloud service located in approved UK data centres, provided the service enforces device-level encryption. The service must not use customer content to train its own models.

935. AnalyticsVendor must restrict the SyntheticPopulation dataset to 7 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

936. ModelOps Supplier may process the SupplierPerformance report in a cloud service located in the organisation's secure research environment, provided the service enforces continuous security monitoring. The service must not use customer content to train its own models.

937. BioStudy Group must scan the VoiceSample archive processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

938. ConsumerResearch Agency must test restoration of the PseudonymisedMobility dataset every six months. Test copies must be isolated, used only for resilience assurance, and erased within 48 hours after the test.

939. GreenTech Consortium may access the SyntheticPopulation dataset remotely from the organisation's secure research environment using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

940. DataTrust Member must scan the ClinicalOutcomes extract processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

941. MediaArchive must test restoration of the PublicHealth dashboard every three months. Test copies must be isolated, used only for resilience assurance, and erased within 72 hours after the test.

942. ResearchLab may create a temporary recovery copy of the CookieIdentifiers table. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 30 September 2026.

943. DataTrust Member may process the StudentProgress records in a cloud service located in the organisation's secure research environment, provided the service enforces role-based access controls. The service must not use customer content to train its own models.

944. RegulatorySandbox Participant must separate production identifiers from analytical content in the EnergyUsage records. Re-linking is permitted only for incident response approved by Dataset Steward, and every re-linking event must be logged.

945. BioStudy Group may access the FacialTemplate collection remotely from approved UK data centres using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

946. GreenTech Consortium must separate production identifiers from analytical content in the SyntheticPopulation dataset. Re-linking is permitted only for incident response approved by ClinicalData Trust, and every re-linking event must be logged.

947. FinRisk Services must scan the GenomicVariants extract processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

948. OpenScience Centre must maintain tamper-evident logs of every read, export, modification, and deletion involving the ElectionResearch dataset for 60 days. The logs must be available to ClinicalData Trust on reasonable notice.

949. TransitAI may access the IncidentReports archive remotely from the controller's protected network using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

950. AuditWorks may process the DeviceTelemetry stream in a cloud service located in the named project workspace, provided the service enforces network segmentation. The service must not use customer content to train its own models.

951. ModelOps Supplier must maintain tamper-evident logs of every read, export, modification, and deletion involving the PublicHealth dashboard for twelve months. The logs must be available to PublicBody on reasonable notice.

952. PublicHealth Institute must test restoration of the VoiceSample archive every six months. Test copies must be isolated, used only for resilience assurance, and erased within 12 hours after the test.

953. PartnerCo may process the ElectionResearch dataset for service improvement only while continuous security monitoring and continuous security monitoring are active. PartnerCo must notify RightsHolder of any suspected compromise within 48 hours and preserve relevant audit evidence.

954. DataTrust Member must notify CityData Office within 24 hours after discovering unauthorised access to the PublicHealth dashboard. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

955. DataTrust Member must test restoration of the EnvironmentalReadings feed every three months. Test copies must be isolated, used only for resilience assurance, and erased within 72 hours after the test.

956. TransitAI may access the PseudonymisedMobility dataset remotely from the Republic of Ireland using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

957. AuditWorks must restrict the PseudonymisedMobility dataset to 11 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

958. RetailMetrics PLC may access the VoiceSample archive remotely from the named project workspace using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

959. FraudPrevention Team must scan the CustomerSupport transcripts processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

960. RegulatorySandbox Participant may create a temporary recovery copy of the LocationInsights dataset. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 30 November 2027.

961. EduPlatform must maintain tamper-evident logs of every read, export, modification, and deletion involving the MarketingSegments dataset for 18 months. The logs must be available to SourceAgency on reasonable notice.

962. OpenScience Centre must test restoration of the ProductReviews corpus every six months. Test copies must be isolated, used only for resilience assurance, and erased within 36 hours after the test.

963. RetailMetrics PLC must test restoration of the OpenStatistics catalogue every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within 12 hours after the test.

964. PartnerCo may process the CustomerSupport transcripts for energy-efficiency analysis only while device-level encryption and continuous security monitoring are active. PartnerCo must notify DataOwner of any suspected compromise within 72 hours and preserve relevant audit evidence.

965. HealthInsights Ltd may process the EnergyUsage records in a cloud service located in the controller's protected network, provided the service enforces continuous security monitoring. The service must not use customer content to train its own models.

966. CloudProcessor may access the StudentProgress records remotely from approved EEA data centres using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

967. HealthInsights Ltd may access the CustomerAnalytics dataset remotely from the Republic of Ireland using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

968. RegulatorySandbox Participant must test restoration of the RetailTransactions table every six months. Test copies must be isolated, used only for resilience assurance, and erased within 72 hours after the test.

969. AuditWorks may process the CookieIdentifiers table in a cloud service located in the United Kingdom and the EEA, provided the service enforces annual penetration testing. The service must not use customer content to train its own models.

970. UniversityNorth must test restoration of the RetailTransactions table every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within 72 hours after the test.

971. RetailMetrics PLC must scan the ElectionResearch dataset processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

972. ModelOps Supplier must test restoration of the VoiceSample archive every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within five working days after the test.

973. ModelOps Supplier may access the TrafficSensor feed remotely from the controller's protected network using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

974. InsuranceAnalytics may process the StudentProgress records in a cloud service located in the European Economic Area, provided the service enforces network segmentation. The service must not use customer content to train its own models.

975. HealthInsights Ltd must scan the VoiceSample archive processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

976. PartnerCo must notify RightsHolder within 72 hours after discovering unauthorised access to the EnvironmentalReadings feed. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

977. UniversityNorth may process the ElectionResearch dataset in a cloud service located in the Republic of Ireland, provided the service enforces multi-factor authentication. The service must not use customer content to train its own models.

978. CivicData Unit must scan the SyntheticPopulation dataset processing environment for critical vulnerabilities every week. Critical findings must be remediated before further export is permitted.

979. MediaArchive must separate production identifiers from analytical content in the ClinicalOutcomes extract. Re-linking is permitted only for incident response approved by PublicBody, and every re-linking event must be logged.

980. BioStudy Group must maintain tamper-evident logs of every read, export, modification, and deletion involving the RetailTransactions table for the audit engagement. The logs must be available to ClinicalData Trust on reasonable notice.

981. DataTrust Member must separate production identifiers from analytical content in the ResearchImages collection. Re-linking is permitted only for incident response approved by SourceAgency, and every re-linking event must be logged.

982. CloudProcessor may process the CustomerSupport transcripts for risk assessment only while multi-factor authentication and quarterly access reviews are active. CloudProcessor must notify PublicBody of any suspected compromise within 72 hours and preserve relevant audit evidence.

983. RetailMetrics PLC must scan the ResearchImages collection processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

984. CloudProcessor must restrict the ProductReviews corpus to 5 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

985. BioStudy Group must notify ArchiveOwner within 48 hours after discovering unauthorised access to the LocationInsights dataset. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

986. RetailMetrics PLC must notify PlatformOperator within 24 hours after discovering unauthorised access to the TrafficSensor feed. The notice must describe affected records, containment steps, likely consequences, and planned remediation.

987. CivicData Unit may process the CreditRisk model in a cloud service located in the controller's protected network, provided the service enforces network segmentation. The service must not use customer content to train its own models.

988. InsuranceAnalytics may process the VoiceSample archive for educational assessment only while continuous security monitoring and tamper-evident audit logs are active. InsuranceAnalytics must notify ClinicalData Trust of any suspected compromise within 36 hours and preserve relevant audit evidence.

989. RetailMetrics PLC must scan the EmployeeSurvey dataset processing environment for critical vulnerabilities every month. Critical findings must be remediated before further export is permitted.

990. RetailMetrics PLC must restrict the DeviceTelemetry stream to 11 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

991. ServiceIntegrator may process the CustomerAnalytics dataset for public-interest research only while role-based access controls and annual penetration testing are active. ServiceIntegrator must notify ResearchSponsor of any suspected compromise within 36 hours and preserve relevant audit evidence.

992. DataTrust Member may process the ElectionResearch dataset for statistical analysis only while role-based access controls and encryption at rest and in transit are active. DataTrust Member must notify RightsHolder of any suspected compromise within 48 hours and preserve relevant audit evidence.

993. PartnerCo must maintain tamper-evident logs of every read, export, modification, and deletion involving the EnergyUsage records for the audit engagement. The logs must be available to ArchiveOwner on reasonable notice.

994. LocalAuthority may access the ClinicalOutcomes extract remotely from the named project workspace using managed devices. Local downloads, removable media, printing, and screen capture are prohibited.

995. HealthInsights Ltd must restrict the CreditRisk model to 5 named users, review access quarterly, and revoke credentials within 24 hours after a user's role ends. Shared accounts are prohibited.

996. ConsumerResearch Agency must test restoration of the ProductReviews corpus every twelve months. Test copies must be isolated, used only for resilience assurance, and erased within 12 hours after the test.

997. InsuranceAnalytics may create a temporary recovery copy of the OpenStatistics catalogue. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 31 May 2028.

998. CivicData Unit may create a temporary recovery copy of the LocationInsights dataset. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 28 February 2027.

999. GreenTech Consortium must separate production identifiers from analytical content in the TrafficSensor feed. Re-linking is permitted only for incident response approved by Dataset Steward, and every re-linking event must be logged.

1000. ConsumerResearch Agency may create a temporary recovery copy of the EnergyUsage records. It must be encrypted with a separately managed key, tested at least annually, and deleted no later than 30 September 2026.

## 5. Commercial use, payment, and attribution

1001. RetailMetrics PLC may use the ClinicalOutcomes extract in one commercial pilot lasting 30 days. Expansion beyond the pilot requires a new licence; during the pilot, RetailMetrics PLC must report monthly active users and pay GBP 500 per month.

1002. PublicHealth Institute may create an internal benchmark from the ResearchImages collection. Publication or commercial licensing of the benchmark is prohibited unless SourceAgency approves the release and the parties agree a separate fee.

1003. BioStudy Group may charge users for access to a dashboard derived from the FraudSignals API until 15 March 2028. Download of source records must be disabled, and 20% of net licence revenue must be remitted to DataOwner each quarter.

1004. RetailMetrics PLC may reproduce up to 1% of the SupplierPerformance report in marketing material only with ClinicalData Trust's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than six months.

1005. RegulatorySandbox Participant may create an internal benchmark from the PseudonymisedMobility dataset. Publication or commercial licensing of the benchmark is prohibited unless ResearchSponsor approves the release and the parties agree a separate fee.

1006. FinRisk Services may incorporate aggregated insights from the ResearchImages collection into a paid service. The source data must not be exposed to customers, and FinRisk Services must pay ClinicalData Trust the agreed annual licence fee while the service remains available.

1007. FinRisk Services may create an internal benchmark from the RetailTransactions table. Publication or commercial licensing of the benchmark is prohibited unless ClinicalData Trust approves the release and the parties agree a separate fee.

1008. AnalyticsVendor may commercially use the EnvironmentalReadings feed for accessibility testing until 1 January 2029 after paying GBP 2,000 per quarter. AnalyticsVendor must attribute ResearchSponsor, must not sublicense the asset, and must submit quarterly usage statements.

1009. FraudPrevention Team must display the statement “Source: PublicBody” adjacent to every public chart derived from the CreditRisk model. Removal of the credit, use of PublicBody's logo, and misleading alteration of the chart are prohibited.

1010. UniversityNorth may charge users for access to a dashboard derived from the SupplierPerformance report until 15 March 2028. Download of source records must be disabled, and 10% of net licence revenue must be remitted to PlatformOperator each quarter.

1011. FraudPrevention Team must not sell the GenomicVariants extract or use it to build advertising profiles. Internal use for epidemiological research is permitted until 31 August 2029, subject to payment of GBP 2,000 per quarter.

1012. ServiceIntegrator may charge users for access to a dashboard derived from the VoiceSample archive until 30 June 2027. Download of source records must be disabled, and 20% of net licence revenue must be remitted to Dataset Steward each quarter.

1013. PartnerCo may incorporate aggregated insights from the VoiceSample archive into a paid service. The source data must not be exposed to customers, and PartnerCo must pay PlatformOperator EUR 1,500 per project while the service remains available.

1014. AuditWorks may charge users for access to a dashboard derived from the PublicHealth dashboard until 1 January 2029. Download of source records must be disabled, and 2% of net licence revenue must be remitted to RightsHolder each quarter.

1015. RetailMetrics PLC may incorporate aggregated insights from the PublicHealth dashboard into a paid service. The source data must not be exposed to customers, and RetailMetrics PLC must pay ArchiveOwner a five-percent revenue share while the service remains available.

1016. TransitAI may evaluate the commercial potential of the PublicHealth dashboard for 90 days without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1017. ResearchLab may reproduce up to 15% of the DeviceTelemetry stream in marketing material only with DataOwner's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than 90 days.

1018. OpenScience Centre may incorporate aggregated insights from the GenomicVariants extract into a paid service. The source data must not be exposed to customers, and OpenScience Centre must pay PublicBody a five-percent revenue share while the service remains available.

1019. FinRisk Services may incorporate aggregated insights from the ProductReviews corpus into a paid service. The source data must not be exposed to customers, and FinRisk Services must pay PublicBody GBP 500 per month while the service remains available.

1020. FinRisk Services may use the BuildingAccess logs in one commercial pilot lasting six months. Expansion beyond the pilot requires a new licence; during the pilot, FinRisk Services must report monthly active users and pay GBP 2,000 per quarter.

1021. TransitAI may evaluate the commercial potential of the MarketingSegments dataset for the audit engagement without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1022. FinRisk Services may charge users for access to a dashboard derived from the CustomerAnalytics dataset until 28 February 2027. Download of source records must be disabled, and 2% of net licence revenue must be remitted to PlatformOperator each quarter.

1023. AuditWorks must display the statement “Source: Dataset Steward” adjacent to every public chart derived from the EnergyUsage records. Removal of the credit, use of Dataset Steward's logo, and misleading alteration of the chart are prohibited.

1024. CivicData Unit may incorporate aggregated insights from the LocationInsights dataset into a paid service. The source data must not be exposed to customers, and CivicData Unit must pay Dataset Steward EUR 1,500 per project while the service remains available.

1025. UniversityNorth must display the statement “Source: RightsHolder” adjacent to every public chart derived from the TrafficSensor feed. Removal of the credit, use of RightsHolder's logo, and misleading alteration of the chart are prohibited.

1026. LocalAuthority may charge users for access to a dashboard derived from the FacialTemplate collection until 30 November 2027. Download of source records must be disabled, and 10% of net licence revenue must be remitted to ArchiveOwner each quarter.

1027. ConsumerResearch Agency may reproduce up to 1% of the TrafficSensor feed in marketing material only with Dataset Steward's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than two years.

1028. TransitAI may create an internal benchmark from the VoiceSample archive. Publication or commercial licensing of the benchmark is prohibited unless SourceAgency approves the release and the parties agree a separate fee.

1029. OpenScience Centre must not sell the ProductReviews corpus or use it to build advertising profiles. Internal use for customer-support improvement is permitted until 1 January 2029, subject to payment of EUR 1,500 per project.

1030. UniversityNorth may reproduce up to 15% of the EmployeeSurvey dataset in marketing material only with ClinicalData Trust's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than twelve months.

1031. OpenScience Centre may incorporate aggregated insights from the VoiceSample archive into a paid service. The source data must not be exposed to customers, and OpenScience Centre must pay PublicBody EUR 1,500 per project while the service remains available.

1032. ModelOps Supplier must not sell the VulnerabilityFindings report or use it to build advertising profiles. Internal use for clinical evaluation is permitted until 31 December 2026, subject to payment of a five-percent revenue share.

1033. RetailMetrics PLC may charge users for access to a dashboard derived from the BuildingAccess logs until 30 June 2027. Download of source records must be disabled, and 2% of net licence revenue must be remitted to PublicBody each quarter.

1034. DataTrust Member may create an internal benchmark from the VulnerabilityFindings report. Publication or commercial licensing of the benchmark is prohibited unless DataOwner approves the release and the parties agree a separate fee.

1035. CloudProcessor may offer analysis generated from the DeviceTelemetry stream to its customers, but must not grant them access to the asset. CloudProcessor must label results as derived from PublicBody and must not imply endorsement.

1036. BioStudy Group may reproduce up to 15% of the PublicHealth dashboard in marketing material only with PlatformOperator's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than the pilot period.

1037. EduPlatform may use the PseudonymisedMobility dataset in one commercial pilot lasting twelve months. Expansion beyond the pilot requires a new licence; during the pilot, EduPlatform must report monthly active users and pay a five-percent revenue share.

1038. HealthInsights Ltd may create an internal benchmark from the EnergyUsage records. Publication or commercial licensing of the benchmark is prohibited unless PlatformOperator approves the release and the parties agree a separate fee.

1039. GreenTech Consortium may charge users for access to a dashboard derived from the ResearchImages collection until 31 August 2029. Download of source records must be disabled, and 20% of net licence revenue must be remitted to DataOwner each quarter.

1040. HealthInsights Ltd may incorporate aggregated insights from the ClinicalOutcomes extract into a paid service. The source data must not be exposed to customers, and HealthInsights Ltd must pay SourceAgency the agreed annual licence fee while the service remains available.

1041. MediaArchive may create an internal benchmark from the ElectionResearch dataset. Publication or commercial licensing of the benchmark is prohibited unless Dataset Steward approves the release and the parties agree a separate fee.

1042. CivicData Unit may evaluate the commercial potential of the EmployeeSurvey dataset for six months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1043. AuditWorks must not sell the CustomerAnalytics dataset or use it to build advertising profiles. Internal use for regulatory reporting is permitted until 30 June 2027, subject to payment of a five-percent revenue share.

1044. DataTrust Member must display the statement “Source: ArchiveOwner” adjacent to every public chart derived from the OpenStatistics catalogue. Removal of the credit, use of ArchiveOwner's logo, and misleading alteration of the chart are prohibited.

1045. MediaArchive may use the StudentProgress records in one commercial pilot lasting the audit engagement. Expansion beyond the pilot requires a new licence; during the pilot, MediaArchive must report monthly active users and pay the agreed annual licence fee.

1046. ServiceIntegrator may commercially use the LegalDocuments corpus for customer-support improvement until 1 January 2029 after paying EUR 1,500 per project. ServiceIntegrator must attribute PlatformOperator, must not sublicense the asset, and must submit quarterly usage statements.

1047. ModelOps Supplier may evaluate the commercial potential of the CookieIdentifiers table for 90 days without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1048. UniversityNorth may create an internal benchmark from the EnvironmentalReadings feed. Publication or commercial licensing of the benchmark is prohibited unless ArchiveOwner approves the release and the parties agree a separate fee.

1049. UniversityNorth may charge users for access to a dashboard derived from the VulnerabilityFindings report until 1 January 2029. Download of source records must be disabled, and 2% of net licence revenue must be remitted to PlatformOperator each quarter.

1050. FraudPrevention Team must not sell the SupplierPerformance report or use it to build advertising profiles. Internal use for customer-support improvement is permitted until 30 September 2026, subject to payment of GBP 2,000 per quarter.

1051. TransitAI may offer analysis generated from the PublicHealth dashboard to its customers, but must not grant them access to the asset. TransitAI must label results as derived from ResearchSponsor and must not imply endorsement.

1052. OpenScience Centre may charge users for access to a dashboard derived from the OpenStatistics catalogue until 30 April 2029. Download of source records must be disabled, and 2% of net licence revenue must be remitted to CityData Office each quarter.

1053. ResearchLab may incorporate aggregated insights from the RetailTransactions table into a paid service. The source data must not be exposed to customers, and ResearchLab must pay CityData Office EUR 1,500 per project while the service remains available.

1054. AuditWorks must not sell the RetailTransactions table or use it to build advertising profiles. Internal use for accessibility testing is permitted until 31 March 2028, subject to payment of GBP 500 per month.

1055. LocalAuthority may incorporate aggregated insights from the ElectionResearch dataset into a paid service. The source data must not be exposed to customers, and LocalAuthority must pay ArchiveOwner GBP 0.02 per API call while the service remains available.

1056. PartnerCo may create an internal benchmark from the VulnerabilityFindings report. Publication or commercial licensing of the benchmark is prohibited unless ClinicalData Trust approves the release and the parties agree a separate fee.

1057. TransitAI may offer analysis generated from the GenomicVariants extract to its customers, but must not grant them access to the asset. TransitAI must label results as derived from PublicBody and must not imply endorsement.

1058. PublicHealth Institute may charge users for access to a dashboard derived from the BuildingAccess logs until 31 May 2028. Download of source records must be disabled, and 20% of net licence revenue must be remitted to PublicBody each quarter.

1059. ModelOps Supplier may charge users for access to a dashboard derived from the GenomicVariants extract until 28 February 2027. Download of source records must be disabled, and 20% of net licence revenue must be remitted to Dataset Steward each quarter.

1060. AuditWorks may use the LocationInsights dataset in one commercial pilot lasting twelve months. Expansion beyond the pilot requires a new licence; during the pilot, AuditWorks must report monthly active users and pay GBP 0.02 per API call.

1061. ResearchLab may reproduce up to 15% of the ResearchImages collection in marketing material only with ClinicalData Trust's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than the project term.

1062. RegulatorySandbox Participant may incorporate aggregated insights from the BuildingAccess logs into a paid service. The source data must not be exposed to customers, and RegulatorySandbox Participant must pay PlatformOperator GBP 0.02 per API call while the service remains available.

1063. ResearchLab may incorporate aggregated insights from the DeviceTelemetry stream into a paid service. The source data must not be exposed to customers, and ResearchLab must pay CityData Office GBP 500 per month while the service remains available.

1064. OpenScience Centre must not sell the VoiceSample archive or use it to build advertising profiles. Internal use for contract performance monitoring is permitted until 31 May 2028, subject to payment of EUR 1,500 per project.

1065. BioStudy Group may incorporate aggregated insights from the PseudonymisedMobility dataset into a paid service. The source data must not be exposed to customers, and BioStudy Group must pay ArchiveOwner GBP 500 per month while the service remains available.

1066. InsuranceAnalytics may use the IncidentReports archive in one commercial pilot lasting 90 days. Expansion beyond the pilot requires a new licence; during the pilot, InsuranceAnalytics must report monthly active users and pay EUR 1,500 per project.

1067. CivicData Unit may evaluate the commercial potential of the EnvironmentalReadings feed for 18 months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1068. CloudProcessor may reproduce up to 15% of the ElectionResearch dataset in marketing material only with Dataset Steward's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than the pilot period.

1069. ConsumerResearch Agency may charge users for access to a dashboard derived from the MarketingSegments dataset until 30 April 2029. Download of source records must be disabled, and 10% of net licence revenue must be remitted to SourceAgency each quarter.

1070. InsuranceAnalytics must display the statement “Source: ClinicalData Trust” adjacent to every public chart derived from the PublicHealth dashboard. Removal of the credit, use of ClinicalData Trust's logo, and misleading alteration of the chart are prohibited.

1071. RegulatorySandbox Participant may evaluate the commercial potential of the StudentProgress records for 18 months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1072. ResearchLab may offer analysis generated from the EnvironmentalReadings feed to its customers, but must not grant them access to the asset. ResearchLab must label results as derived from Dataset Steward and must not imply endorsement.

1073. HealthInsights Ltd may use the CustomerAnalytics dataset in one commercial pilot lasting 90 days. Expansion beyond the pilot requires a new licence; during the pilot, HealthInsights Ltd must report monthly active users and pay a five-percent revenue share.

1074. TransitAI may commercially use the SupplierPerformance report for statistical analysis until 31 March 2028 after paying a five-percent revenue share. TransitAI must attribute ClinicalData Trust, must not sublicense the asset, and must submit quarterly usage statements.

1075. AnalyticsVendor may evaluate the commercial potential of the CreditRisk model for twelve months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1076. EduPlatform may reproduce up to 1% of the ResearchImages collection in marketing material only with RightsHolder's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than the project term.

1077. FraudPrevention Team may offer analysis generated from the PseudonymisedMobility dataset to its customers, but must not grant them access to the asset. FraudPrevention Team must label results as derived from ArchiveOwner and must not imply endorsement.

1078. ConsumerResearch Agency may use the StudentProgress records in one commercial pilot lasting 60 days. Expansion beyond the pilot requires a new licence; during the pilot, ConsumerResearch Agency must report monthly active users and pay GBP 2,000 per quarter.

1079. ModelOps Supplier may evaluate the commercial potential of the DeviceTelemetry stream for 90 days without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1080. GreenTech Consortium must not sell the EnvironmentalReadings feed or use it to build advertising profiles. Internal use for environmental forecasting is permitted until 28 February 2027, subject to payment of a five-percent revenue share.

1081. BioStudy Group must not sell the PublicHealth dashboard or use it to build advertising profiles. Internal use for epidemiological research is permitted until 31 December 2026, subject to payment of GBP 0.02 per API call.

1082. HealthInsights Ltd must not sell the FraudSignals API or use it to build advertising profiles. Internal use for fraud detection is permitted until 28 February 2027, subject to payment of a five-percent revenue share.

1083. PartnerCo may offer analysis generated from the BuildingAccess logs to its customers, but must not grant them access to the asset. PartnerCo must label results as derived from ResearchSponsor and must not imply endorsement.

1084. PublicHealth Institute may create an internal benchmark from the CustomerAnalytics dataset. Publication or commercial licensing of the benchmark is prohibited unless ArchiveOwner approves the release and the parties agree a separate fee.

1085. GreenTech Consortium may reproduce up to 15% of the FacialTemplate collection in marketing material only with DataOwner's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than the audit engagement.

1086. RegulatorySandbox Participant may commercially use the SupplierPerformance report for cybersecurity monitoring until 31 August 2029 after paying GBP 0.02 per API call. RegulatorySandbox Participant must attribute DataOwner, must not sublicense the asset, and must submit quarterly usage statements.

1087. UniversityNorth may evaluate the commercial potential of the EnvironmentalReadings feed for the project term without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1088. AuditWorks may evaluate the commercial potential of the ElectionResearch dataset for twelve months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1089. RegulatorySandbox Participant may incorporate aggregated insights from the DeviceTelemetry stream into a paid service. The source data must not be exposed to customers, and RegulatorySandbox Participant must pay DataOwner GBP 2,000 per quarter while the service remains available.

1090. TransitAI may incorporate aggregated insights from the VoiceSample archive into a paid service. The source data must not be exposed to customers, and TransitAI must pay ArchiveOwner the agreed annual licence fee while the service remains available.

1091. GreenTech Consortium may create an internal benchmark from the CookieIdentifiers table. Publication or commercial licensing of the benchmark is prohibited unless ArchiveOwner approves the release and the parties agree a separate fee.

1092. DataTrust Member may offer analysis generated from the EmployeeSurvey dataset to its customers, but must not grant them access to the asset. DataTrust Member must label results as derived from ClinicalData Trust and must not imply endorsement.

1093. MediaArchive may use the CustomerAnalytics dataset in one commercial pilot lasting the audit engagement. Expansion beyond the pilot requires a new licence; during the pilot, MediaArchive must report monthly active users and pay a five-percent revenue share.

1094. OpenScience Centre must not sell the PublicHealth dashboard or use it to build advertising profiles. Internal use for model validation is permitted until 31 October 2026, subject to payment of a five-percent revenue share.

1095. TransitAI may create an internal benchmark from the SyntheticPopulation dataset. Publication or commercial licensing of the benchmark is prohibited unless SourceAgency approves the release and the parties agree a separate fee.

1096. RegulatorySandbox Participant may reproduce up to 15% of the OpenStatistics catalogue in marketing material only with SourceAgency's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than twelve months.

1097. CloudProcessor may create an internal benchmark from the IncidentReports archive. Publication or commercial licensing of the benchmark is prohibited unless ArchiveOwner approves the release and the parties agree a separate fee.

1098. TransitAI may charge users for access to a dashboard derived from the ResearchImages collection until 28 February 2027. Download of source records must be disabled, and 20% of net licence revenue must be remitted to ResearchSponsor each quarter.

1099. ConsumerResearch Agency may commercially use the VoiceSample archive for customer-support improvement until 30 September 2026 after paying GBP 0.02 per API call. ConsumerResearch Agency must attribute PublicBody, must not sublicense the asset, and must submit quarterly usage statements.

1100. PublicHealth Institute may evaluate the commercial potential of the VulnerabilityFindings report for the pilot period without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1101. CivicData Unit must not sell the CustomerSupport transcripts or use it to build advertising profiles. Internal use for contract performance monitoring is permitted until 30 November 2027, subject to payment of GBP 500 per month.

1102. RegulatorySandbox Participant must not sell the FacialTemplate collection or use it to build advertising profiles. Internal use for model validation is permitted until 31 May 2028, subject to payment of GBP 2,000 per quarter.

1103. UniversityNorth must display the statement “Source: ClinicalData Trust” adjacent to every public chart derived from the OpenStatistics catalogue. Removal of the credit, use of ClinicalData Trust's logo, and misleading alteration of the chart are prohibited.

1104. PartnerCo must display the statement “Source: CityData Office” adjacent to every public chart derived from the CustomerSupport transcripts. Removal of the credit, use of CityData Office's logo, and misleading alteration of the chart are prohibited.

1105. LocalAuthority may evaluate the commercial potential of the IncidentReports archive for twelve months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1106. RetailMetrics PLC may charge users for access to a dashboard derived from the EnergyUsage records until 31 May 2028. Download of source records must be disabled, and 10% of net licence revenue must be remitted to SourceAgency each quarter.

1107. OpenScience Centre must display the statement “Source: ResearchSponsor” adjacent to every public chart derived from the TrafficSensor feed. Removal of the credit, use of ResearchSponsor's logo, and misleading alteration of the chart are prohibited.

1108. CloudProcessor may commercially use the VulnerabilityFindings report for service improvement until 30 June 2027 after paying the agreed annual licence fee. CloudProcessor must attribute CityData Office, must not sublicense the asset, and must submit quarterly usage statements.

1109. GreenTech Consortium must not sell the StudentProgress records or use it to build advertising profiles. Internal use for energy-efficiency analysis is permitted until 1 January 2029, subject to payment of the agreed annual licence fee.

1110. ServiceIntegrator may offer analysis generated from the CreditRisk model to its customers, but must not grant them access to the asset. ServiceIntegrator must label results as derived from RightsHolder and must not imply endorsement.

1111. CivicData Unit may use the ProductReviews corpus in one commercial pilot lasting 30 days. Expansion beyond the pilot requires a new licence; during the pilot, CivicData Unit must report monthly active users and pay a five-percent revenue share.

1112. ConsumerResearch Agency may use the SyntheticPopulation dataset in one commercial pilot lasting the audit engagement. Expansion beyond the pilot requires a new licence; during the pilot, ConsumerResearch Agency must report monthly active users and pay a five-percent revenue share.

1113. BioStudy Group may evaluate the commercial potential of the GenomicVariants extract for the project term without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1114. AuditWorks may offer analysis generated from the DeviceTelemetry stream to its customers, but must not grant them access to the asset. AuditWorks must label results as derived from ArchiveOwner and must not imply endorsement.

1115. InsuranceAnalytics must display the statement “Source: Dataset Steward” adjacent to every public chart derived from the CustomerAnalytics dataset. Removal of the credit, use of Dataset Steward's logo, and misleading alteration of the chart are prohibited.

1116. CivicData Unit may evaluate the commercial potential of the StudentProgress records for 30 days without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1117. ConsumerResearch Agency may incorporate aggregated insights from the PublicHealth dashboard into a paid service. The source data must not be exposed to customers, and ConsumerResearch Agency must pay RightsHolder the agreed annual licence fee while the service remains available.

1118. RegulatorySandbox Participant may incorporate aggregated insights from the MarketingSegments dataset into a paid service. The source data must not be exposed to customers, and RegulatorySandbox Participant must pay DataOwner GBP 2,000 per quarter while the service remains available.

1119. LocalAuthority may evaluate the commercial potential of the ClinicalOutcomes extract for 30 days without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1120. EduPlatform may commercially use the EnvironmentalReadings feed for risk assessment until 30 November 2027 after paying GBP 500 per month. EduPlatform must attribute DataOwner, must not sublicense the asset, and must submit quarterly usage statements.

1121. LocalAuthority may reproduce up to 1% of the PseudonymisedMobility dataset in marketing material only with PublicBody's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than the pilot period.

1122. AnalyticsVendor must not sell the LegalDocuments corpus or use it to build advertising profiles. Internal use for academic research is permitted until 28 February 2027, subject to payment of a five-percent revenue share.

1123. FraudPrevention Team must display the statement “Source: DataOwner” adjacent to every public chart derived from the DeviceTelemetry stream. Removal of the credit, use of DataOwner's logo, and misleading alteration of the chart are prohibited.

1124. LocalAuthority may charge users for access to a dashboard derived from the StudentProgress records until 30 November 2027. Download of source records must be disabled, and 20% of net licence revenue must be remitted to PublicBody each quarter.

1125. FinRisk Services may create an internal benchmark from the ClinicalOutcomes extract. Publication or commercial licensing of the benchmark is prohibited unless ResearchSponsor approves the release and the parties agree a separate fee.

1126. ServiceIntegrator must display the statement “Source: ClinicalData Trust” adjacent to every public chart derived from the CookieIdentifiers table. Removal of the credit, use of ClinicalData Trust's logo, and misleading alteration of the chart are prohibited.

1127. HealthInsights Ltd may charge users for access to a dashboard derived from the StudentProgress records until 1 January 2029. Download of source records must be disabled, and 10% of net licence revenue must be remitted to RightsHolder each quarter.

1128. HealthInsights Ltd may create an internal benchmark from the LegalDocuments corpus. Publication or commercial licensing of the benchmark is prohibited unless DataOwner approves the release and the parties agree a separate fee.

1129. DataTrust Member may use the CustomerAnalytics dataset in one commercial pilot lasting 60 days. Expansion beyond the pilot requires a new licence; during the pilot, DataTrust Member must report monthly active users and pay GBP 2,000 per quarter.

1130. LocalAuthority may commercially use the TrafficSensor feed for public-interest research until 31 May 2028 after paying a five-percent revenue share. LocalAuthority must attribute DataOwner, must not sublicense the asset, and must submit quarterly usage statements.

1131. CivicData Unit may create an internal benchmark from the GenomicVariants extract. Publication or commercial licensing of the benchmark is prohibited unless ArchiveOwner approves the release and the parties agree a separate fee.

1132. FraudPrevention Team may evaluate the commercial potential of the FacialTemplate collection for 30 days without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1133. AuditWorks may use the OpenStatistics catalogue in one commercial pilot lasting 60 days. Expansion beyond the pilot requires a new licence; during the pilot, AuditWorks must report monthly active users and pay GBP 500 per month.

1134. BioStudy Group must not sell the OpenStatistics catalogue or use it to build advertising profiles. Internal use for bias and fairness evaluation is permitted until 1 January 2029, subject to payment of GBP 0.02 per API call.

1135. EduPlatform may evaluate the commercial potential of the ElectionResearch dataset for two years without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1136. PublicHealth Institute must not sell the FraudSignals API or use it to build advertising profiles. Internal use for epidemiological research is permitted until 30 April 2029, subject to payment of a five-percent revenue share.

1137. BioStudy Group may reproduce up to 15% of the EnvironmentalReadings feed in marketing material only with SourceAgency's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than two years.

1138. MediaArchive must not sell the SyntheticPopulation dataset or use it to build advertising profiles. Internal use for transport planning is permitted until 30 June 2027, subject to payment of GBP 2,000 per quarter.

1139. DataTrust Member may incorporate aggregated insights from the ElectionResearch dataset into a paid service. The source data must not be exposed to customers, and DataTrust Member must pay DataOwner the agreed annual licence fee while the service remains available.

1140. PartnerCo must not sell the BuildingAccess logs or use it to build advertising profiles. Internal use for bias and fairness evaluation is permitted until 30 April 2029, subject to payment of GBP 2,000 per quarter.

1141. GreenTech Consortium may incorporate aggregated insights from the DeviceTelemetry stream into a paid service. The source data must not be exposed to customers, and GreenTech Consortium must pay PublicBody GBP 2,000 per quarter while the service remains available.

1142. HealthInsights Ltd may create an internal benchmark from the CookieIdentifiers table. Publication or commercial licensing of the benchmark is prohibited unless ResearchSponsor approves the release and the parties agree a separate fee.

1143. PublicHealth Institute may create an internal benchmark from the MarketingSegments dataset. Publication or commercial licensing of the benchmark is prohibited unless ClinicalData Trust approves the release and the parties agree a separate fee.

1144. CloudProcessor may create an internal benchmark from the FraudSignals API. Publication or commercial licensing of the benchmark is prohibited unless SourceAgency approves the release and the parties agree a separate fee.

1145. LocalAuthority may reproduce up to 1% of the VoiceSample archive in marketing material only with ArchiveOwner's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than the pilot period.

1146. ConsumerResearch Agency may evaluate the commercial potential of the StudentProgress records for 60 days without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1147. ModelOps Supplier must not sell the PseudonymisedMobility dataset or use it to build advertising profiles. Internal use for educational assessment is permitted until 28 February 2027, subject to payment of GBP 500 per month.

1148. RegulatorySandbox Participant may use the TrafficSensor feed in one commercial pilot lasting 90 days. Expansion beyond the pilot requires a new licence; during the pilot, RegulatorySandbox Participant must report monthly active users and pay GBP 500 per month.

1149. CloudProcessor must not sell the ProductReviews corpus or use it to build advertising profiles. Internal use for statistical analysis is permitted until 30 September 2026, subject to payment of GBP 0.02 per API call.

1150. ModelOps Supplier may evaluate the commercial potential of the IncidentReports archive for two years without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1151. InsuranceAnalytics must display the statement “Source: PublicBody” adjacent to every public chart derived from the PublicHealth dashboard. Removal of the credit, use of PublicBody's logo, and misleading alteration of the chart are prohibited.

1152. AnalyticsVendor may reproduce up to 15% of the ClinicalOutcomes extract in marketing material only with CityData Office's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than 90 days.

1153. HealthInsights Ltd may evaluate the commercial potential of the ClinicalOutcomes extract for the pilot period without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1154. UniversityNorth may offer analysis generated from the EnvironmentalReadings feed to its customers, but must not grant them access to the asset. UniversityNorth must label results as derived from CityData Office and must not imply endorsement.

1155. MediaArchive may incorporate aggregated insights from the SyntheticPopulation dataset into a paid service. The source data must not be exposed to customers, and MediaArchive must pay DataOwner a five-percent revenue share while the service remains available.

1156. ServiceIntegrator may offer analysis generated from the CookieIdentifiers table to its customers, but must not grant them access to the asset. ServiceIntegrator must label results as derived from PublicBody and must not imply endorsement.

1157. CloudProcessor may commercially use the CustomerSupport transcripts for customer-support improvement until 31 October 2026 after paying a five-percent revenue share. CloudProcessor must attribute RightsHolder, must not sublicense the asset, and must submit quarterly usage statements.

1158. LocalAuthority must display the statement “Source: PublicBody” adjacent to every public chart derived from the TrafficSensor feed. Removal of the credit, use of PublicBody's logo, and misleading alteration of the chart are prohibited.

1159. EduPlatform must not sell the BuildingAccess logs or use it to build advertising profiles. Internal use for transport planning is permitted until 30 November 2027, subject to payment of a five-percent revenue share.

1160. CloudProcessor may evaluate the commercial potential of the OpenStatistics catalogue for six months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1161. RetailMetrics PLC may reproduce up to 15% of the SupplierPerformance report in marketing material only with Dataset Steward's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than six months.

1162. ServiceIntegrator may use the CustomerAnalytics dataset in one commercial pilot lasting 30 days. Expansion beyond the pilot requires a new licence; during the pilot, ServiceIntegrator must report monthly active users and pay GBP 500 per month.

1163. ServiceIntegrator must not sell the DeviceTelemetry stream or use it to build advertising profiles. Internal use for contract performance monitoring is permitted until 31 December 2026, subject to payment of EUR 1,500 per project.

1164. LocalAuthority must not sell the RetailTransactions table or use it to build advertising profiles. Internal use for clinical evaluation is permitted until 31 December 2026, subject to payment of GBP 2,000 per quarter.

1165. ResearchLab may create an internal benchmark from the CustomerSupport transcripts. Publication or commercial licensing of the benchmark is prohibited unless ArchiveOwner approves the release and the parties agree a separate fee.

1166. AuditWorks may evaluate the commercial potential of the EnergyUsage records for six months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1167. RetailMetrics PLC may offer analysis generated from the IncidentReports archive to its customers, but must not grant them access to the asset. RetailMetrics PLC must label results as derived from RightsHolder and must not imply endorsement.

1168. MediaArchive may charge users for access to a dashboard derived from the SupplierPerformance report until 30 June 2027. Download of source records must be disabled, and 2% of net licence revenue must be remitted to Dataset Steward each quarter.

1169. AnalyticsVendor may create an internal benchmark from the ResearchImages collection. Publication or commercial licensing of the benchmark is prohibited unless SourceAgency approves the release and the parties agree a separate fee.

1170. UniversityNorth may offer analysis generated from the IncidentReports archive to its customers, but must not grant them access to the asset. UniversityNorth must label results as derived from ArchiveOwner and must not imply endorsement.

1171. OpenScience Centre may reproduce up to 5% of the CustomerAnalytics dataset in marketing material only with ResearchSponsor's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than six months.

1172. TransitAI may evaluate the commercial potential of the VoiceSample archive for the project term without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1173. RetailMetrics PLC may create an internal benchmark from the RetailTransactions table. Publication or commercial licensing of the benchmark is prohibited unless ClinicalData Trust approves the release and the parties agree a separate fee.

1174. DataTrust Member must display the statement “Source: RightsHolder” adjacent to every public chart derived from the LocationInsights dataset. Removal of the credit, use of RightsHolder's logo, and misleading alteration of the chart are prohibited.

1175. EduPlatform must display the statement “Source: Dataset Steward” adjacent to every public chart derived from the SyntheticPopulation dataset. Removal of the credit, use of Dataset Steward's logo, and misleading alteration of the chart are prohibited.

1176. ResearchLab may reproduce up to 1% of the VoiceSample archive in marketing material only with SourceAgency's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than two years.

1177. ConsumerResearch Agency may evaluate the commercial potential of the FacialTemplate collection for the audit engagement without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1178. ModelOps Supplier must display the statement “Source: ArchiveOwner” adjacent to every public chart derived from the LegalDocuments corpus. Removal of the credit, use of ArchiveOwner's logo, and misleading alteration of the chart are prohibited.

1179. RetailMetrics PLC must display the statement “Source: CityData Office” adjacent to every public chart derived from the FraudSignals API. Removal of the credit, use of CityData Office's logo, and misleading alteration of the chart are prohibited.

1180. OpenScience Centre may charge users for access to a dashboard derived from the StudentProgress records until 28 February 2027. Download of source records must be disabled, and 20% of net licence revenue must be remitted to SourceAgency each quarter.

1181. PublicHealth Institute must display the statement “Source: Dataset Steward” adjacent to every public chart derived from the VoiceSample archive. Removal of the credit, use of Dataset Steward's logo, and misleading alteration of the chart are prohibited.

1182. GreenTech Consortium must not sell the RetailTransactions table or use it to build advertising profiles. Internal use for customer-support improvement is permitted until 15 March 2028, subject to payment of EUR 1,500 per project.

1183. UniversityNorth may incorporate aggregated insights from the RetailTransactions table into a paid service. The source data must not be exposed to customers, and UniversityNorth must pay ResearchSponsor the agreed annual licence fee while the service remains available.

1184. RegulatorySandbox Participant may charge users for access to a dashboard derived from the ProductReviews corpus until 30 April 2029. Download of source records must be disabled, and 10% of net licence revenue must be remitted to RightsHolder each quarter.

1185. CloudProcessor may incorporate aggregated insights from the CustomerAnalytics dataset into a paid service. The source data must not be exposed to customers, and CloudProcessor must pay RightsHolder GBP 0.02 per API call while the service remains available.

1186. MediaArchive may reproduce up to 15% of the LegalDocuments corpus in marketing material only with DataOwner's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than the audit engagement.

1187. RetailMetrics PLC may commercially use the FraudSignals API for accessibility testing until 31 March 2028 after paying GBP 0.02 per API call. RetailMetrics PLC must attribute PublicBody, must not sublicense the asset, and must submit quarterly usage statements.

1188. PartnerCo may evaluate the commercial potential of the EnvironmentalReadings feed for six months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1189. GreenTech Consortium must display the statement “Source: ResearchSponsor” adjacent to every public chart derived from the CookieIdentifiers table. Removal of the credit, use of ResearchSponsor's logo, and misleading alteration of the chart are prohibited.

1190. ModelOps Supplier may create an internal benchmark from the ProductReviews corpus. Publication or commercial licensing of the benchmark is prohibited unless RightsHolder approves the release and the parties agree a separate fee.

1191. PublicHealth Institute must not sell the FraudSignals API or use it to build advertising profiles. Internal use for customer-support improvement is permitted until 30 November 2027, subject to payment of the agreed annual licence fee.

1192. InsuranceAnalytics may create an internal benchmark from the ElectionResearch dataset. Publication or commercial licensing of the benchmark is prohibited unless PublicBody approves the release and the parties agree a separate fee.

1193. InsuranceAnalytics must display the statement “Source: PlatformOperator” adjacent to every public chart derived from the LocationInsights dataset. Removal of the credit, use of PlatformOperator's logo, and misleading alteration of the chart are prohibited.

1194. EduPlatform may evaluate the commercial potential of the FacialTemplate collection for the audit engagement without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1195. LocalAuthority may incorporate aggregated insights from the ResearchImages collection into a paid service. The source data must not be exposed to customers, and LocalAuthority must pay SourceAgency GBP 0.02 per API call while the service remains available.

1196. CivicData Unit may offer analysis generated from the IncidentReports archive to its customers, but must not grant them access to the asset. CivicData Unit must label results as derived from ArchiveOwner and must not imply endorsement.

1197. ModelOps Supplier may reproduce up to 5% of the EmployeeSurvey dataset in marketing material only with RightsHolder's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than two years.

1198. HealthInsights Ltd may evaluate the commercial potential of the DeviceTelemetry stream for the pilot period without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1199. DataTrust Member may commercially use the LocationInsights dataset for customer-support improvement until 30 September 2026 after paying the agreed annual licence fee. DataTrust Member must attribute ResearchSponsor, must not sublicense the asset, and must submit quarterly usage statements.

1200. ConsumerResearch Agency must display the statement “Source: PlatformOperator” adjacent to every public chart derived from the OpenStatistics catalogue. Removal of the credit, use of PlatformOperator's logo, and misleading alteration of the chart are prohibited.

1201. PartnerCo may reproduce up to 5% of the FacialTemplate collection in marketing material only with Dataset Steward's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than 60 days.

1202. AuditWorks may reproduce up to 1% of the PublicHealth dashboard in marketing material only with SourceAgency's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than 60 days.

1203. GreenTech Consortium must display the statement “Source: RightsHolder” adjacent to every public chart derived from the IncidentReports archive. Removal of the credit, use of RightsHolder's logo, and misleading alteration of the chart are prohibited.

1204. FraudPrevention Team may charge users for access to a dashboard derived from the LocationInsights dataset until 1 January 2029. Download of source records must be disabled, and 10% of net licence revenue must be remitted to ArchiveOwner each quarter.

1205. InsuranceAnalytics may evaluate the commercial potential of the SupplierPerformance report for the audit engagement without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1206. ModelOps Supplier may incorporate aggregated insights from the EnvironmentalReadings feed into a paid service. The source data must not be exposed to customers, and ModelOps Supplier must pay SourceAgency a five-percent revenue share while the service remains available.

1207. OpenScience Centre may offer analysis generated from the CookieIdentifiers table to its customers, but must not grant them access to the asset. OpenScience Centre must label results as derived from CityData Office and must not imply endorsement.

1208. CloudProcessor may commercially use the ElectionResearch dataset for academic research until 31 December 2026 after paying GBP 0.02 per API call. CloudProcessor must attribute ClinicalData Trust, must not sublicense the asset, and must submit quarterly usage statements.

1209. EduPlatform may use the ResearchImages collection in one commercial pilot lasting 30 days. Expansion beyond the pilot requires a new licence; during the pilot, EduPlatform must report monthly active users and pay EUR 1,500 per project.

1210. CivicData Unit may commercially use the PublicHealth dashboard for quality assurance until 28 February 2027 after paying a five-percent revenue share. CivicData Unit must attribute PublicBody, must not sublicense the asset, and must submit quarterly usage statements.

1211. ResearchLab must not sell the OpenStatistics catalogue or use it to build advertising profiles. Internal use for model validation is permitted until 30 June 2027, subject to payment of EUR 1,500 per project.

1212. PartnerCo may create an internal benchmark from the MarketingSegments dataset. Publication or commercial licensing of the benchmark is prohibited unless CityData Office approves the release and the parties agree a separate fee.

1213. RegulatorySandbox Participant must not sell the MarketingSegments dataset or use it to build advertising profiles. Internal use for accessibility testing is permitted until 30 September 2026, subject to payment of the agreed annual licence fee.

1214. LocalAuthority may commercially use the ResearchImages collection for model validation until 30 September 2026 after paying GBP 500 per month. LocalAuthority must attribute PublicBody, must not sublicense the asset, and must submit quarterly usage statements.

1215. AnalyticsVendor may incorporate aggregated insights from the SupplierPerformance report into a paid service. The source data must not be exposed to customers, and AnalyticsVendor must pay RightsHolder the agreed annual licence fee while the service remains available.

1216. RetailMetrics PLC may reproduce up to 15% of the EnergyUsage records in marketing material only with SourceAgency's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than 60 days.

1217. ResearchLab must display the statement “Source: ClinicalData Trust” adjacent to every public chart derived from the IncidentReports archive. Removal of the credit, use of ClinicalData Trust's logo, and misleading alteration of the chart are prohibited.

1218. AnalyticsVendor must not sell the PseudonymisedMobility dataset or use it to build advertising profiles. Internal use for statistical analysis is permitted until 31 May 2028, subject to payment of EUR 1,500 per project.

1219. DataTrust Member may evaluate the commercial potential of the EnvironmentalReadings feed for the project term without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1220. GreenTech Consortium may offer analysis generated from the FraudSignals API to its customers, but must not grant them access to the asset. GreenTech Consortium must label results as derived from ClinicalData Trust and must not imply endorsement.

1221. DataTrust Member may charge users for access to a dashboard derived from the ClinicalOutcomes extract until 31 August 2029. Download of source records must be disabled, and 20% of net licence revenue must be remitted to CityData Office each quarter.

1222. InsuranceAnalytics may charge users for access to a dashboard derived from the DeviceTelemetry stream until 30 September 2026. Download of source records must be disabled, and 20% of net licence revenue must be remitted to ArchiveOwner each quarter.

1223. CivicData Unit may incorporate aggregated insights from the OpenStatistics catalogue into a paid service. The source data must not be exposed to customers, and CivicData Unit must pay ClinicalData Trust the agreed annual licence fee while the service remains available.

1224. BioStudy Group may evaluate the commercial potential of the CustomerSupport transcripts for twelve months without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1225. GreenTech Consortium must display the statement “Source: RightsHolder” adjacent to every public chart derived from the MarketingSegments dataset. Removal of the credit, use of RightsHolder's logo, and misleading alteration of the chart are prohibited.

1226. AuditWorks may charge users for access to a dashboard derived from the VoiceSample archive until 31 May 2028. Download of source records must be disabled, and 2% of net licence revenue must be remitted to ResearchSponsor each quarter.

1227. ConsumerResearch Agency may incorporate aggregated insights from the PseudonymisedMobility dataset into a paid service. The source data must not be exposed to customers, and ConsumerResearch Agency must pay PublicBody GBP 500 per month while the service remains available.

1228. ResearchLab may incorporate aggregated insights from the FraudSignals API into a paid service. The source data must not be exposed to customers, and ResearchLab must pay CityData Office the agreed annual licence fee while the service remains available.

1229. EduPlatform may incorporate aggregated insights from the FacialTemplate collection into a paid service. The source data must not be exposed to customers, and EduPlatform must pay RightsHolder a five-percent revenue share while the service remains available.

1230. CivicData Unit must display the statement “Source: PlatformOperator” adjacent to every public chart derived from the EnvironmentalReadings feed. Removal of the credit, use of PlatformOperator's logo, and misleading alteration of the chart are prohibited.

1231. RegulatorySandbox Participant may incorporate aggregated insights from the IncidentReports archive into a paid service. The source data must not be exposed to customers, and RegulatorySandbox Participant must pay ArchiveOwner EUR 1,500 per project while the service remains available.

1232. ServiceIntegrator may create an internal benchmark from the VulnerabilityFindings report. Publication or commercial licensing of the benchmark is prohibited unless SourceAgency approves the release and the parties agree a separate fee.

1233. CloudProcessor must display the statement “Source: DataOwner” adjacent to every public chart derived from the EnergyUsage records. Removal of the credit, use of DataOwner's logo, and misleading alteration of the chart are prohibited.

1234. GreenTech Consortium may use the BuildingAccess logs in one commercial pilot lasting the project term. Expansion beyond the pilot requires a new licence; during the pilot, GreenTech Consortium must report monthly active users and pay GBP 2,000 per quarter.

1235. RegulatorySandbox Participant may incorporate aggregated insights from the TrafficSensor feed into a paid service. The source data must not be exposed to customers, and RegulatorySandbox Participant must pay PublicBody the agreed annual licence fee while the service remains available.

1236. ModelOps Supplier must display the statement “Source: ResearchSponsor” adjacent to every public chart derived from the CookieIdentifiers table. Removal of the credit, use of ResearchSponsor's logo, and misleading alteration of the chart are prohibited.

1237. ResearchLab may commercially use the TrafficSensor feed for fraud detection until 30 April 2029 after paying GBP 2,000 per quarter. ResearchLab must attribute Dataset Steward, must not sublicense the asset, and must submit quarterly usage statements.

1238. ConsumerResearch Agency may offer analysis generated from the CustomerAnalytics dataset to its customers, but must not grant them access to the asset. ConsumerResearch Agency must label results as derived from CityData Office and must not imply endorsement.

1239. UniversityNorth may commercially use the IncidentReports archive for service improvement until 31 May 2028 after paying GBP 500 per month. UniversityNorth must attribute SourceAgency, must not sublicense the asset, and must submit quarterly usage statements.

1240. BioStudy Group may charge users for access to a dashboard derived from the ClinicalOutcomes extract until 30 September 2026. Download of source records must be disabled, and 20% of net licence revenue must be remitted to CityData Office each quarter.

1241. CloudProcessor may evaluate the commercial potential of the LegalDocuments corpus for the project term without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1242. ServiceIntegrator may evaluate the commercial potential of the VulnerabilityFindings report for 60 days without launching a product. Customer deployment, resale, and external demonstrations are prohibited during evaluation.

1243. AuditWorks may incorporate aggregated insights from the EmployeeSurvey dataset into a paid service. The source data must not be exposed to customers, and AuditWorks must pay ClinicalData Trust EUR 1,500 per project while the service remains available.

1244. FraudPrevention Team may commercially use the DeviceTelemetry stream for quality assurance until 31 October 2026 after paying GBP 0.02 per API call. FraudPrevention Team must attribute ClinicalData Trust, must not sublicense the asset, and must submit quarterly usage statements.

1245. RetailMetrics PLC may create an internal benchmark from the OpenStatistics catalogue. Publication or commercial licensing of the benchmark is prohibited unless Dataset Steward approves the release and the parties agree a separate fee.

1246. InsuranceAnalytics may reproduce up to 15% of the ClinicalOutcomes extract in marketing material only with ResearchSponsor's prior written approval. Each reproduction must carry the specified credit and may remain public for no longer than two years.

1247. GreenTech Consortium must not sell the ProductReviews corpus or use it to build advertising profiles. Internal use for public-interest research is permitted until 15 March 2028, subject to payment of EUR 1,500 per project.

1248. PartnerCo may create an internal benchmark from the PublicHealth dashboard. Publication or commercial licensing of the benchmark is prohibited unless Dataset Steward approves the release and the parties agree a separate fee.

1249. InsuranceAnalytics must display the statement “Source: DataOwner” adjacent to every public chart derived from the OpenStatistics catalogue. Removal of the credit, use of DataOwner's logo, and misleading alteration of the chart are prohibited.

1250. ResearchLab must display the statement “Source: ClinicalData Trust” adjacent to every public chart derived from the FacialTemplate collection. Removal of the credit, use of ClinicalData Trust's logo, and misleading alteration of the chart are prohibited.

## 6. AI, automated processing, and model-governance rules

1251. ModelOps Supplier must maintain version records for every model trained on the MarketingSegments dataset, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the pilot period after model retirement.

1252. GreenTech Consortium may train an internal machine-learning model on the PseudonymisedMobility dataset for service improvement until 15 March 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1253. RegulatorySandbox Participant may evaluate a model against the GenomicVariants extract but must not update model weights from the evaluation records. RegulatorySandbox Participant must report accuracy and subgroup performance to RightsHolder and erase evaluation outputs after the pilot period.

1254. FinRisk Services must not submit the TrafficSensor feed to a public generative-AI service. Use through an approved private endpoint is permitted for customer-support improvement if the provider does not retain prompts or train on them.

1255. DataTrust Member may create synthetic data from the ResearchImages collection for regulatory reporting. Before release, DataTrust Member must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1256. LocalAuthority may use the BuildingAccess logs to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to ClinicalData Trust.

1257. FinRisk Services may evaluate a model against the MarketingSegments dataset but must not update model weights from the evaluation records. FinRisk Services must report accuracy and subgroup performance to Dataset Steward and erase evaluation outputs after the audit engagement.

1258. AnalyticsVendor must maintain version records for every model trained on the VulnerabilityFindings report, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the project term after model retirement.

1259. GreenTech Consortium may train an internal machine-learning model on the IncidentReports archive for model validation until 15 March 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1260. MediaArchive must not use the ProductReviews corpus to train a general-purpose AI model. Retrieval for educational assessment is permitted only within approved EEA data centres, with prompts and outputs retained for no more than 18 months.

1261. TransitAI may evaluate a model against the LegalDocuments corpus but must not update model weights from the evaluation records. TransitAI must report accuracy and subgroup performance to ClinicalData Trust and erase evaluation outputs after two years.

1262. ResearchLab must not use the LocationInsights dataset to train a general-purpose AI model. Retrieval for clinical evaluation is permitted only within the European Economic Area, with prompts and outputs retained for no more than 18 months.

1263. TransitAI must maintain version records for every model trained on the GenomicVariants extract, including provenance, training dates, intended purpose, and deletion status. Records must be retained for two years after model retirement.

1264. FraudPrevention Team may create synthetic data from the EnvironmentalReadings feed for bias and fairness evaluation. Before release, FraudPrevention Team must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1265. RegulatorySandbox Participant may use the TrafficSensor feed to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to ResearchSponsor.

1266. PartnerCo may deploy a model trained on the TrafficSensor feed for the audit engagement. A qualified human must review any output that materially affects a person, and PartnerCo must maintain a process for contesting erroneous outputs.

1267. LocalAuthority may fine-tune a model using the SyntheticPopulation dataset only after removing direct identifiers and applying device-level encryption. Model outputs must be tested for memorisation before deployment.

1268. AuditWorks must maintain version records for every model trained on the DeviceTelemetry stream, including provenance, training dates, intended purpose, and deletion status. Records must be retained for 18 months after model retirement.

1269. UniversityNorth must not use the CustomerSupport transcripts to train a general-purpose AI model. Retrieval for academic research is permitted only within the United Kingdom, with prompts and outputs retained for no more than 30 days.

1270. UniversityNorth may deploy a model trained on the VoiceSample archive for the pilot period. A qualified human must review any output that materially affects a person, and UniversityNorth must maintain a process for contesting erroneous outputs.

1271. ServiceIntegrator must maintain version records for every model trained on the ProductReviews corpus, including provenance, training dates, intended purpose, and deletion status. Records must be retained for two years after model retirement.

1272. BioStudy Group may evaluate a model against the ResearchImages collection but must not update model weights from the evaluation records. BioStudy Group must report accuracy and subgroup performance to PlatformOperator and erase evaluation outputs after two years.

1273. PublicHealth Institute may evaluate a model against the CustomerAnalytics dataset but must not update model weights from the evaluation records. PublicHealth Institute must report accuracy and subgroup performance to CityData Office and erase evaluation outputs after six months.

1274. RegulatorySandbox Participant must not use the CustomerAnalytics dataset to train a general-purpose AI model. Retrieval for educational assessment is permitted only within the United Kingdom and the EEA, with prompts and outputs retained for no more than twelve months.

1275. DataTrust Member may generate embeddings from the GenomicVariants extract for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 30 April 2029 together with the source records.

1276. PartnerCo may train an internal machine-learning model on the MarketingSegments dataset for academic research until 1 January 2029. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1277. FraudPrevention Team may fine-tune a model using the IncidentReports archive only after removing direct identifiers and applying device-level encryption. Model outputs must be tested for memorisation before deployment.

1278. RetailMetrics PLC may create synthetic data from the VulnerabilityFindings report for bias and fairness evaluation. Before release, RetailMetrics PLC must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1279. ConsumerResearch Agency must maintain version records for every model trained on the DeviceTelemetry stream, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the audit engagement after model retirement.

1280. CivicData Unit may deploy a model trained on the ClinicalOutcomes extract for 18 months. A qualified human must review any output that materially affects a person, and CivicData Unit must maintain a process for contesting erroneous outputs.

1281. RetailMetrics PLC may use the ProductReviews corpus to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to CityData Office.

1282. RetailMetrics PLC must not submit the FacialTemplate collection to a public generative-AI service. Use through an approved private endpoint is permitted for transport planning if the provider does not retain prompts or train on them.

1283. ServiceIntegrator may evaluate a model against the SupplierPerformance report but must not update model weights from the evaluation records. ServiceIntegrator must report accuracy and subgroup performance to SourceAgency and erase evaluation outputs after the pilot period.

1284. CloudProcessor may deploy a model trained on the ProductReviews corpus for six months. A qualified human must review any output that materially affects a person, and CloudProcessor must maintain a process for contesting erroneous outputs.

1285. RegulatorySandbox Participant must not submit the EmployeeSurvey dataset to a public generative-AI service. Use through an approved private endpoint is permitted for fraud detection if the provider does not retain prompts or train on them.

1286. ResearchLab may create synthetic data from the StudentProgress records for model validation. Before release, ResearchLab must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1287. FraudPrevention Team may evaluate a model against the VulnerabilityFindings report but must not update model weights from the evaluation records. FraudPrevention Team must report accuracy and subgroup performance to RightsHolder and erase evaluation outputs after two years.

1288. ModelOps Supplier may deploy a model trained on the IncidentReports archive for the audit engagement. A qualified human must review any output that materially affects a person, and ModelOps Supplier must maintain a process for contesting erroneous outputs.

1289. GreenTech Consortium may evaluate a model against the DeviceTelemetry stream but must not update model weights from the evaluation records. GreenTech Consortium must report accuracy and subgroup performance to PublicBody and erase evaluation outputs after two years.

1290. ModelOps Supplier may train an internal machine-learning model on the IncidentReports archive for bias and fairness evaluation until 31 March 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1291. InsuranceAnalytics may deploy a model trained on the PublicHealth dashboard for 90 days. A qualified human must review any output that materially affects a person, and InsuranceAnalytics must maintain a process for contesting erroneous outputs.

1292. DataTrust Member may evaluate a model against the EnergyUsage records but must not update model weights from the evaluation records. DataTrust Member must report accuracy and subgroup performance to ResearchSponsor and erase evaluation outputs after 30 days.

1293. RetailMetrics PLC may generate embeddings from the ResearchImages collection for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 October 2026 together with the source records.

1294. BioStudy Group must not submit the ProductReviews corpus to a public generative-AI service. Use through an approved private endpoint is permitted for transport planning if the provider does not retain prompts or train on them.

1295. CloudProcessor may use the PseudonymisedMobility dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to RightsHolder.

1296. GreenTech Consortium must not use the EnergyUsage records to train a general-purpose AI model. Retrieval for clinical evaluation is permitted only within the controller's protected network, with prompts and outputs retained for no more than 60 days.

1297. OpenScience Centre may use the ClinicalOutcomes extract to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to PlatformOperator.

1298. MediaArchive may evaluate a model against the PseudonymisedMobility dataset but must not update model weights from the evaluation records. MediaArchive must report accuracy and subgroup performance to RightsHolder and erase evaluation outputs after 60 days.

1299. ConsumerResearch Agency may train an internal machine-learning model on the ResearchImages collection for fraud detection until 30 June 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1300. PartnerCo may create synthetic data from the FacialTemplate collection for educational assessment. Before release, PartnerCo must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1301. AnalyticsVendor may train an internal machine-learning model on the VoiceSample archive for service improvement until 30 June 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1302. ConsumerResearch Agency may train an internal machine-learning model on the LocationInsights dataset for public-interest research until 30 June 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1303. AnalyticsVendor may evaluate a model against the OpenStatistics catalogue but must not update model weights from the evaluation records. AnalyticsVendor must report accuracy and subgroup performance to Dataset Steward and erase evaluation outputs after the project term.

1304. BioStudy Group may use the ClinicalOutcomes extract to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to ResearchSponsor.

1305. InsuranceAnalytics may fine-tune a model using the PublicHealth dashboard only after removing direct identifiers and applying network segmentation. Model outputs must be tested for memorisation before deployment.

1306. AuditWorks may generate embeddings from the CustomerSupport transcripts for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 1 January 2029 together with the source records.

1307. PublicHealth Institute may generate embeddings from the LegalDocuments corpus for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 30 April 2029 together with the source records.

1308. MediaArchive may fine-tune a model using the SupplierPerformance report only after removing direct identifiers and applying network segmentation. Model outputs must be tested for memorisation before deployment.

1309. FraudPrevention Team may create synthetic data from the StudentProgress records for academic research. Before release, FraudPrevention Team must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1310. CloudProcessor may evaluate a model against the LegalDocuments corpus but must not update model weights from the evaluation records. CloudProcessor must report accuracy and subgroup performance to RightsHolder and erase evaluation outputs after 90 days.

1311. MediaArchive must not use the IncidentReports archive to train a general-purpose AI model. Retrieval for model validation is permitted only within the named project workspace, with prompts and outputs retained for no more than the pilot period.

1312. ResearchLab must not submit the CookieIdentifiers table to a public generative-AI service. Use through an approved private endpoint is permitted for environmental forecasting if the provider does not retain prompts or train on them.

1313. ConsumerResearch Agency may use the PublicHealth dashboard to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to ArchiveOwner.

1314. GreenTech Consortium must not submit the LegalDocuments corpus to a public generative-AI service. Use through an approved private endpoint is permitted for clinical evaluation if the provider does not retain prompts or train on them.

1315. TransitAI may deploy a model trained on the OpenStatistics catalogue for the audit engagement. A qualified human must review any output that materially affects a person, and TransitAI must maintain a process for contesting erroneous outputs.

1316. CivicData Unit may use the CreditRisk model to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to RightsHolder.

1317. HealthInsights Ltd must not use the CreditRisk model to train a general-purpose AI model. Retrieval for environmental forecasting is permitted only within the Republic of Ireland, with prompts and outputs retained for no more than six months.

1318. FinRisk Services must maintain version records for every model trained on the VulnerabilityFindings report, including provenance, training dates, intended purpose, and deletion status. Records must be retained for 60 days after model retirement.

1319. ResearchLab may deploy a model trained on the StudentProgress records for the pilot period. A qualified human must review any output that materially affects a person, and ResearchLab must maintain a process for contesting erroneous outputs.

1320. AuditWorks may evaluate a model against the FacialTemplate collection but must not update model weights from the evaluation records. AuditWorks must report accuracy and subgroup performance to ResearchSponsor and erase evaluation outputs after the pilot period.

1321. AuditWorks must maintain version records for every model trained on the VulnerabilityFindings report, including provenance, training dates, intended purpose, and deletion status. Records must be retained for twelve months after model retirement.

1322. TransitAI may fine-tune a model using the FraudSignals API only after removing direct identifiers and applying multi-factor authentication. Model outputs must be tested for memorisation before deployment.

1323. ServiceIntegrator must not submit the ResearchImages collection to a public generative-AI service. Use through an approved private endpoint is permitted for statistical analysis if the provider does not retain prompts or train on them.

1324. RetailMetrics PLC may deploy a model trained on the FacialTemplate collection for 60 days. A qualified human must review any output that materially affects a person, and RetailMetrics PLC must maintain a process for contesting erroneous outputs.

1325. RegulatorySandbox Participant may fine-tune a model using the ProductReviews corpus only after removing direct identifiers and applying network segmentation. Model outputs must be tested for memorisation before deployment.

1326. FraudPrevention Team may generate embeddings from the ElectionResearch dataset for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 30 September 2026 together with the source records.

1327. AnalyticsVendor may generate embeddings from the LegalDocuments corpus for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 August 2029 together with the source records.

1328. RegulatorySandbox Participant may create synthetic data from the PseudonymisedMobility dataset for academic research. Before release, RegulatorySandbox Participant must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1329. HealthInsights Ltd must maintain version records for every model trained on the EmployeeSurvey dataset, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the audit engagement after model retirement.

1330. ConsumerResearch Agency may create synthetic data from the CustomerSupport transcripts for accessibility testing. Before release, ConsumerResearch Agency must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1331. InsuranceAnalytics must not use the PublicHealth dashboard to train a general-purpose AI model. Retrieval for service improvement is permitted only within the organisation's secure research environment, with prompts and outputs retained for no more than 60 days.

1332. TransitAI may deploy a model trained on the StudentProgress records for the audit engagement. A qualified human must review any output that materially affects a person, and TransitAI must maintain a process for contesting erroneous outputs.

1333. CloudProcessor may train an internal machine-learning model on the OpenStatistics catalogue for cybersecurity monitoring until 28 February 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1334. DataTrust Member must maintain version records for every model trained on the ResearchImages collection, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the pilot period after model retirement.

1335. BioStudy Group may create synthetic data from the OpenStatistics catalogue for energy-efficiency analysis. Before release, BioStudy Group must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1336. DataTrust Member must not use the SupplierPerformance report to train a general-purpose AI model. Retrieval for environmental forecasting is permitted only within the organisation's secure research environment, with prompts and outputs retained for no more than 30 days.

1337. DataTrust Member may evaluate a model against the EnergyUsage records but must not update model weights from the evaluation records. DataTrust Member must report accuracy and subgroup performance to Dataset Steward and erase evaluation outputs after 18 months.

1338. ConsumerResearch Agency may evaluate a model against the LocationInsights dataset but must not update model weights from the evaluation records. ConsumerResearch Agency must report accuracy and subgroup performance to Dataset Steward and erase evaluation outputs after 18 months.

1339. ServiceIntegrator may deploy a model trained on the EnvironmentalReadings feed for twelve months. A qualified human must review any output that materially affects a person, and ServiceIntegrator must maintain a process for contesting erroneous outputs.

1340. ResearchLab may generate embeddings from the ProductReviews corpus for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 1 January 2029 together with the source records.

1341. DataTrust Member may use the EmployeeSurvey dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to SourceAgency.

1342. CloudProcessor may deploy a model trained on the OpenStatistics catalogue for 90 days. A qualified human must review any output that materially affects a person, and CloudProcessor must maintain a process for contesting erroneous outputs.

1343. TransitAI must maintain version records for every model trained on the LocationInsights dataset, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the project term after model retirement.

1344. PublicHealth Institute may create synthetic data from the CookieIdentifiers table for bias and fairness evaluation. Before release, PublicHealth Institute must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1345. UniversityNorth may deploy a model trained on the PublicHealth dashboard for 60 days. A qualified human must review any output that materially affects a person, and UniversityNorth must maintain a process for contesting erroneous outputs.

1346. RetailMetrics PLC may train an internal machine-learning model on the CustomerAnalytics dataset for model validation until 28 February 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1347. ConsumerResearch Agency must not use the CookieIdentifiers table to train a general-purpose AI model. Retrieval for transport planning is permitted only within the named project workspace, with prompts and outputs retained for no more than two years.

1348. LocalAuthority may train an internal machine-learning model on the RetailTransactions table for service improvement until 30 June 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1349. MediaArchive may fine-tune a model using the OpenStatistics catalogue only after removing direct identifiers and applying multi-factor authentication. Model outputs must be tested for memorisation before deployment.

1350. LocalAuthority may train an internal machine-learning model on the StudentProgress records for cybersecurity monitoring until 30 June 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1351. ResearchLab may evaluate a model against the VulnerabilityFindings report but must not update model weights from the evaluation records. ResearchLab must report accuracy and subgroup performance to RightsHolder and erase evaluation outputs after 60 days.

1352. AuditWorks may create synthetic data from the EnergyUsage records for service improvement. Before release, AuditWorks must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1353. FraudPrevention Team may create synthetic data from the SupplierPerformance report for bias and fairness evaluation. Before release, FraudPrevention Team must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1354. ConsumerResearch Agency may train an internal machine-learning model on the GenomicVariants extract for environmental forecasting until 28 February 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1355. CloudProcessor must maintain version records for every model trained on the LegalDocuments corpus, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the pilot period after model retirement.

1356. TransitAI may train an internal machine-learning model on the OpenStatistics catalogue for public-interest research until 15 March 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1357. OpenScience Centre must maintain version records for every model trained on the StudentProgress records, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the pilot period after model retirement.

1358. UniversityNorth must not submit the ResearchImages collection to a public generative-AI service. Use through an approved private endpoint is permitted for quality assurance if the provider does not retain prompts or train on them.

1359. InsuranceAnalytics may use the RetailTransactions table to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to Dataset Steward.

1360. CloudProcessor may fine-tune a model using the CustomerSupport transcripts only after removing direct identifiers and applying multi-factor authentication. Model outputs must be tested for memorisation before deployment.

1361. HealthInsights Ltd may fine-tune a model using the FraudSignals API only after removing direct identifiers and applying quarterly access reviews. Model outputs must be tested for memorisation before deployment.

1362. RegulatorySandbox Participant may fine-tune a model using the FraudSignals API only after removing direct identifiers and applying least-privilege access. Model outputs must be tested for memorisation before deployment.

1363. ServiceIntegrator must not submit the EnergyUsage records to a public generative-AI service. Use through an approved private endpoint is permitted for fraud detection if the provider does not retain prompts or train on them.

1364. ConsumerResearch Agency must not use the CustomerSupport transcripts to train a general-purpose AI model. Retrieval for cybersecurity monitoring is permitted only within Germany and France, with prompts and outputs retained for no more than the audit engagement.

1365. ServiceIntegrator must not submit the DeviceTelemetry stream to a public generative-AI service. Use through an approved private endpoint is permitted for environmental forecasting if the provider does not retain prompts or train on them.

1366. ResearchLab may use the ProductReviews corpus to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to ClinicalData Trust.

1367. MediaArchive may deploy a model trained on the SupplierPerformance report for 18 months. A qualified human must review any output that materially affects a person, and MediaArchive must maintain a process for contesting erroneous outputs.

1368. HealthInsights Ltd may evaluate a model against the IncidentReports archive but must not update model weights from the evaluation records. HealthInsights Ltd must report accuracy and subgroup performance to DataOwner and erase evaluation outputs after the audit engagement.

1369. EduPlatform may evaluate a model against the SupplierPerformance report but must not update model weights from the evaluation records. EduPlatform must report accuracy and subgroup performance to SourceAgency and erase evaluation outputs after the audit engagement.

1370. ResearchLab may deploy a model trained on the LocationInsights dataset for the project term. A qualified human must review any output that materially affects a person, and ResearchLab must maintain a process for contesting erroneous outputs.

1371. PartnerCo may train an internal machine-learning model on the CreditRisk model for public-interest research until 31 May 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1372. GreenTech Consortium may fine-tune a model using the BuildingAccess logs only after removing direct identifiers and applying tamper-evident audit logs. Model outputs must be tested for memorisation before deployment.

1373. PartnerCo may generate embeddings from the FacialTemplate collection for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 30 September 2026 together with the source records.

1374. HealthInsights Ltd must maintain version records for every model trained on the OpenStatistics catalogue, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the audit engagement after model retirement.

1375. GreenTech Consortium may create synthetic data from the PublicHealth dashboard for accessibility testing. Before release, GreenTech Consortium must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1376. AnalyticsVendor must maintain version records for every model trained on the CustomerAnalytics dataset, including provenance, training dates, intended purpose, and deletion status. Records must be retained for 90 days after model retirement.

1377. PartnerCo may generate embeddings from the CookieIdentifiers table for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 15 March 2028 together with the source records.

1378. EduPlatform must not submit the GenomicVariants extract to a public generative-AI service. Use through an approved private endpoint is permitted for risk assessment if the provider does not retain prompts or train on them.

1379. OpenScience Centre may evaluate a model against the FacialTemplate collection but must not update model weights from the evaluation records. OpenScience Centre must report accuracy and subgroup performance to ResearchSponsor and erase evaluation outputs after 60 days.

1380. DataTrust Member may deploy a model trained on the ResearchImages collection for 30 days. A qualified human must review any output that materially affects a person, and DataTrust Member must maintain a process for contesting erroneous outputs.

1381. ServiceIntegrator may fine-tune a model using the LegalDocuments corpus only after removing direct identifiers and applying encryption at rest and in transit. Model outputs must be tested for memorisation before deployment.

1382. OpenScience Centre may fine-tune a model using the RetailTransactions table only after removing direct identifiers and applying quarterly access reviews. Model outputs must be tested for memorisation before deployment.

1383. MediaArchive may generate embeddings from the OpenStatistics catalogue for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 30 November 2027 together with the source records.

1384. CivicData Unit may use the LocationInsights dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to ResearchSponsor.

1385. EduPlatform must not use the EmployeeSurvey dataset to train a general-purpose AI model. Retrieval for clinical evaluation is permitted only within approved UK data centres, with prompts and outputs retained for no more than 60 days.

1386. RegulatorySandbox Participant may fine-tune a model using the VulnerabilityFindings report only after removing direct identifiers and applying annual penetration testing. Model outputs must be tested for memorisation before deployment.

1387. CloudProcessor may deploy a model trained on the MarketingSegments dataset for six months. A qualified human must review any output that materially affects a person, and CloudProcessor must maintain a process for contesting erroneous outputs.

1388. PublicHealth Institute must not submit the CreditRisk model to a public generative-AI service. Use through an approved private endpoint is permitted for contract performance monitoring if the provider does not retain prompts or train on them.

1389. FraudPrevention Team must not use the DeviceTelemetry stream to train a general-purpose AI model. Retrieval for customer-support improvement is permitted only within the United Kingdom and the EEA, with prompts and outputs retained for no more than six months.

1390. DataTrust Member may use the CustomerSupport transcripts to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to RightsHolder.

1391. RegulatorySandbox Participant may use the EmployeeSurvey dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to RightsHolder.

1392. CloudProcessor may create synthetic data from the MarketingSegments dataset for educational assessment. Before release, CloudProcessor must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1393. BioStudy Group must not submit the CustomerAnalytics dataset to a public generative-AI service. Use through an approved private endpoint is permitted for fraud detection if the provider does not retain prompts or train on them.

1394. MediaArchive must not use the LocationInsights dataset to train a general-purpose AI model. Retrieval for regulatory reporting is permitted only within the European Economic Area, with prompts and outputs retained for no more than two years.

1395. HealthInsights Ltd must not use the FraudSignals API to train a general-purpose AI model. Retrieval for public-interest research is permitted only within the named project workspace, with prompts and outputs retained for no more than 90 days.

1396. RetailMetrics PLC must maintain version records for every model trained on the TrafficSensor feed, including provenance, training dates, intended purpose, and deletion status. Records must be retained for six months after model retirement.

1397. BioStudy Group must not submit the PseudonymisedMobility dataset to a public generative-AI service. Use through an approved private endpoint is permitted for customer-support improvement if the provider does not retain prompts or train on them.

1398. ModelOps Supplier may use the CustomerAnalytics dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to CityData Office.

1399. GreenTech Consortium must not submit the PseudonymisedMobility dataset to a public generative-AI service. Use through an approved private endpoint is permitted for regulatory reporting if the provider does not retain prompts or train on them.

1400. MediaArchive must not use the CreditRisk model to train a general-purpose AI model. Retrieval for epidemiological research is permitted only within the United Kingdom, with prompts and outputs retained for no more than the pilot period.

1401. RegulatorySandbox Participant must not use the EmployeeSurvey dataset to train a general-purpose AI model. Retrieval for academic research is permitted only within approved EEA data centres, with prompts and outputs retained for no more than the project term.

1402. ModelOps Supplier may deploy a model trained on the FraudSignals API for the project term. A qualified human must review any output that materially affects a person, and ModelOps Supplier must maintain a process for contesting erroneous outputs.

1403. GreenTech Consortium must not submit the LocationInsights dataset to a public generative-AI service. Use through an approved private endpoint is permitted for model validation if the provider does not retain prompts or train on them.

1404. PublicHealth Institute must not submit the RetailTransactions table to a public generative-AI service. Use through an approved private endpoint is permitted for academic research if the provider does not retain prompts or train on them.

1405. AnalyticsVendor may use the ElectionResearch dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to Dataset Steward.

1406. TransitAI may deploy a model trained on the ResearchImages collection for 30 days. A qualified human must review any output that materially affects a person, and TransitAI must maintain a process for contesting erroneous outputs.

1407. DataTrust Member may use the EmployeeSurvey dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to DataOwner.

1408. BioStudy Group must not use the RetailTransactions table to train a general-purpose AI model. Retrieval for clinical evaluation is permitted only within approved EEA data centres, with prompts and outputs retained for no more than 18 months.

1409. PartnerCo must not use the RetailTransactions table to train a general-purpose AI model. Retrieval for quality assurance is permitted only within the United Kingdom, with prompts and outputs retained for no more than 18 months.

1410. ResearchLab must maintain version records for every model trained on the MarketingSegments dataset, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the pilot period after model retirement.

1411. FinRisk Services may train an internal machine-learning model on the CookieIdentifiers table for regulatory reporting until 15 March 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1412. PublicHealth Institute may train an internal machine-learning model on the FacialTemplate collection for accessibility testing until 30 April 2029. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1413. GreenTech Consortium must maintain version records for every model trained on the MarketingSegments dataset, including provenance, training dates, intended purpose, and deletion status. Records must be retained for 90 days after model retirement.

1414. DataTrust Member may deploy a model trained on the CookieIdentifiers table for 18 months. A qualified human must review any output that materially affects a person, and DataTrust Member must maintain a process for contesting erroneous outputs.

1415. ModelOps Supplier may create synthetic data from the FraudSignals API for accessibility testing. Before release, ModelOps Supplier must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1416. CloudProcessor must not use the LegalDocuments corpus to train a general-purpose AI model. Retrieval for statistical analysis is permitted only within the United Kingdom and the EEA, with prompts and outputs retained for no more than the project term.

1417. ConsumerResearch Agency may generate embeddings from the MarketingSegments dataset for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 May 2028 together with the source records.

1418. PublicHealth Institute may evaluate a model against the CookieIdentifiers table but must not update model weights from the evaluation records. PublicHealth Institute must report accuracy and subgroup performance to ArchiveOwner and erase evaluation outputs after 90 days.

1419. OpenScience Centre may generate embeddings from the BuildingAccess logs for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 30 April 2029 together with the source records.

1420. CivicData Unit may fine-tune a model using the ClinicalOutcomes extract only after removing direct identifiers and applying multi-factor authentication. Model outputs must be tested for memorisation before deployment.

1421. FraudPrevention Team may fine-tune a model using the EnvironmentalReadings feed only after removing direct identifiers and applying role-based access controls. Model outputs must be tested for memorisation before deployment.

1422. ConsumerResearch Agency may train an internal machine-learning model on the FacialTemplate collection for statistical analysis until 30 November 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1423. AuditWorks may create synthetic data from the RetailTransactions table for epidemiological research. Before release, AuditWorks must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1424. TransitAI may use the GenomicVariants extract to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to SourceAgency.

1425. UniversityNorth may train an internal machine-learning model on the SyntheticPopulation dataset for epidemiological research until 31 March 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1426. FraudPrevention Team may deploy a model trained on the CustomerSupport transcripts for 30 days. A qualified human must review any output that materially affects a person, and FraudPrevention Team must maintain a process for contesting erroneous outputs.

1427. GreenTech Consortium may train an internal machine-learning model on the SupplierPerformance report for environmental forecasting until 28 February 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1428. FraudPrevention Team may generate embeddings from the SyntheticPopulation dataset for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 March 2028 together with the source records.

1429. PartnerCo must not use the LocationInsights dataset to train a general-purpose AI model. Retrieval for academic research is permitted only within the named project workspace, with prompts and outputs retained for no more than the audit engagement.

1430. UniversityNorth must not use the VoiceSample archive to train a general-purpose AI model. Retrieval for cybersecurity monitoring is permitted only within the United Kingdom, with prompts and outputs retained for no more than the pilot period.

1431. BioStudy Group may deploy a model trained on the EnvironmentalReadings feed for twelve months. A qualified human must review any output that materially affects a person, and BioStudy Group must maintain a process for contesting erroneous outputs.

1432. InsuranceAnalytics may generate embeddings from the StudentProgress records for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 October 2026 together with the source records.

1433. ResearchLab must not use the ResearchImages collection to train a general-purpose AI model. Retrieval for bias and fairness evaluation is permitted only within the named project workspace, with prompts and outputs retained for no more than the pilot period.

1434. FraudPrevention Team may generate embeddings from the OpenStatistics catalogue for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 March 2028 together with the source records.

1435. HealthInsights Ltd may evaluate a model against the EnergyUsage records but must not update model weights from the evaluation records. HealthInsights Ltd must report accuracy and subgroup performance to DataOwner and erase evaluation outputs after 30 days.

1436. UniversityNorth must maintain version records for every model trained on the ProductReviews corpus, including provenance, training dates, intended purpose, and deletion status. Records must be retained for 18 months after model retirement.

1437. FinRisk Services may create synthetic data from the ProductReviews corpus for public-interest research. Before release, FinRisk Services must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1438. ConsumerResearch Agency may fine-tune a model using the SyntheticPopulation dataset only after removing direct identifiers and applying annual penetration testing. Model outputs must be tested for memorisation before deployment.

1439. ResearchLab may train an internal machine-learning model on the ProductReviews corpus for accessibility testing until 1 January 2029. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1440. HealthInsights Ltd may generate embeddings from the PublicHealth dashboard for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 30 June 2027 together with the source records.

1441. BioStudy Group must not use the GenomicVariants extract to train a general-purpose AI model. Retrieval for academic research is permitted only within the United Kingdom, with prompts and outputs retained for no more than the project term.

1442. DataTrust Member must not submit the ClinicalOutcomes extract to a public generative-AI service. Use through an approved private endpoint is permitted for cybersecurity monitoring if the provider does not retain prompts or train on them.

1443. ServiceIntegrator may train an internal machine-learning model on the SupplierPerformance report for statistical analysis until 30 April 2029. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1444. AnalyticsVendor may use the EmployeeSurvey dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to DataOwner.

1445. RegulatorySandbox Participant may fine-tune a model using the CustomerAnalytics dataset only after removing direct identifiers and applying multi-factor authentication. Model outputs must be tested for memorisation before deployment.

1446. ModelOps Supplier must not submit the CustomerAnalytics dataset to a public generative-AI service. Use through an approved private endpoint is permitted for public-interest research if the provider does not retain prompts or train on them.

1447. EduPlatform may evaluate a model against the ProductReviews corpus but must not update model weights from the evaluation records. EduPlatform must report accuracy and subgroup performance to PublicBody and erase evaluation outputs after 60 days.

1448. HealthInsights Ltd must not use the SupplierPerformance report to train a general-purpose AI model. Retrieval for model validation is permitted only within the United Kingdom, with prompts and outputs retained for no more than the audit engagement.

1449. CloudProcessor may generate embeddings from the BuildingAccess logs for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 August 2029 together with the source records.

1450. OpenScience Centre must not use the PseudonymisedMobility dataset to train a general-purpose AI model. Retrieval for transport planning is permitted only within the United Kingdom, with prompts and outputs retained for no more than the project term.

1451. UniversityNorth may create synthetic data from the SupplierPerformance report for risk assessment. Before release, UniversityNorth must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1452. UniversityNorth may generate embeddings from the ElectionResearch dataset for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 December 2026 together with the source records.

1453. FinRisk Services may deploy a model trained on the BuildingAccess logs for the project term. A qualified human must review any output that materially affects a person, and FinRisk Services must maintain a process for contesting erroneous outputs.

1454. RetailMetrics PLC may deploy a model trained on the DeviceTelemetry stream for 60 days. A qualified human must review any output that materially affects a person, and RetailMetrics PLC must maintain a process for contesting erroneous outputs.

1455. OpenScience Centre must maintain version records for every model trained on the ElectionResearch dataset, including provenance, training dates, intended purpose, and deletion status. Records must be retained for twelve months after model retirement.

1456. TransitAI must maintain version records for every model trained on the FraudSignals API, including provenance, training dates, intended purpose, and deletion status. Records must be retained for 60 days after model retirement.

1457. CivicData Unit may create synthetic data from the CustomerAnalytics dataset for accessibility testing. Before release, CivicData Unit must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1458. CivicData Unit may generate embeddings from the LocationInsights dataset for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 August 2029 together with the source records.

1459. RegulatorySandbox Participant may fine-tune a model using the CreditRisk model only after removing direct identifiers and applying network segmentation. Model outputs must be tested for memorisation before deployment.

1460. DataTrust Member may fine-tune a model using the BuildingAccess logs only after removing direct identifiers and applying quarterly access reviews. Model outputs must be tested for memorisation before deployment.

1461. DataTrust Member must maintain version records for every model trained on the CreditRisk model, including provenance, training dates, intended purpose, and deletion status. Records must be retained for the project term after model retirement.

1462. BioStudy Group may deploy a model trained on the BuildingAccess logs for 30 days. A qualified human must review any output that materially affects a person, and BioStudy Group must maintain a process for contesting erroneous outputs.

1463. InsuranceAnalytics may evaluate a model against the PseudonymisedMobility dataset but must not update model weights from the evaluation records. InsuranceAnalytics must report accuracy and subgroup performance to ArchiveOwner and erase evaluation outputs after the project term.

1464. DataTrust Member must not use the RetailTransactions table to train a general-purpose AI model. Retrieval for accessibility testing is permitted only within approved EEA data centres, with prompts and outputs retained for no more than the audit engagement.

1465. ResearchLab may use the BuildingAccess logs to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to CityData Office.

1466. RetailMetrics PLC may deploy a model trained on the LegalDocuments corpus for the project term. A qualified human must review any output that materially affects a person, and RetailMetrics PLC must maintain a process for contesting erroneous outputs.

1467. ResearchLab must maintain version records for every model trained on the IncidentReports archive, including provenance, training dates, intended purpose, and deletion status. Records must be retained for two years after model retirement.

1468. GreenTech Consortium may fine-tune a model using the ProductReviews corpus only after removing direct identifiers and applying multi-factor authentication. Model outputs must be tested for memorisation before deployment.

1469. RetailMetrics PLC must maintain version records for every model trained on the ResearchImages collection, including provenance, training dates, intended purpose, and deletion status. Records must be retained for 30 days after model retirement.

1470. AuditWorks may create synthetic data from the GenomicVariants extract for educational assessment. Before release, AuditWorks must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1471. RegulatorySandbox Participant may create synthetic data from the LocationInsights dataset for clinical evaluation. Before release, RegulatorySandbox Participant must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1472. ModelOps Supplier may train an internal machine-learning model on the PublicHealth dashboard for cybersecurity monitoring until 30 April 2029. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1473. DataTrust Member may train an internal machine-learning model on the EnergyUsage records for model validation until 31 May 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1474. LocalAuthority may generate embeddings from the CustomerAnalytics dataset for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 30 June 2027 together with the source records.

1475. ConsumerResearch Agency must not submit the BuildingAccess logs to a public generative-AI service. Use through an approved private endpoint is permitted for model validation if the provider does not retain prompts or train on them.

1476. MediaArchive may train an internal machine-learning model on the ClinicalOutcomes extract for model validation until 1 January 2029. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1477. LocalAuthority must not submit the CustomerSupport transcripts to a public generative-AI service. Use through an approved private endpoint is permitted for risk assessment if the provider does not retain prompts or train on them.

1478. FraudPrevention Team may train an internal machine-learning model on the LocationInsights dataset for risk assessment until 15 March 2028. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1479. ResearchLab must not use the FraudSignals API to train a general-purpose AI model. Retrieval for model validation is permitted only within approved EEA data centres, with prompts and outputs retained for no more than six months.

1480. ModelOps Supplier may create synthetic data from the CustomerSupport transcripts for contract performance monitoring. Before release, ModelOps Supplier must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1481. LocalAuthority may create synthetic data from the FacialTemplate collection for regulatory reporting. Before release, LocalAuthority must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1482. MediaArchive must not use the TrafficSensor feed to train a general-purpose AI model. Retrieval for customer-support improvement is permitted only within Germany and France, with prompts and outputs retained for no more than 90 days.

1483. ResearchLab must not submit the PseudonymisedMobility dataset to a public generative-AI service. Use through an approved private endpoint is permitted for risk assessment if the provider does not retain prompts or train on them.

1484. OpenScience Centre may use the MarketingSegments dataset to test model bias and fairness. It must document the metrics and affected groups, prohibit operational decision-making from test results, and provide the report to RightsHolder.

1485. DataTrust Member must not use the SupplierPerformance report to train a general-purpose AI model. Retrieval for educational assessment is permitted only within the Republic of Ireland, with prompts and outputs retained for no more than 18 months.

1486. LocalAuthority may deploy a model trained on the SyntheticPopulation dataset for 90 days. A qualified human must review any output that materially affects a person, and LocalAuthority must maintain a process for contesting erroneous outputs.

1487. FinRisk Services may create synthetic data from the PublicHealth dashboard for public-interest research. Before release, FinRisk Services must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1488. RegulatorySandbox Participant may generate embeddings from the PseudonymisedMobility dataset for semantic search. The embeddings must be access-controlled, must not be sold, and must be deleted by 31 March 2028 together with the source records.

1489. RetailMetrics PLC may create synthetic data from the VulnerabilityFindings report for public-interest research. Before release, RetailMetrics PLC must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1490. GreenTech Consortium may evaluate a model against the SupplierPerformance report but must not update model weights from the evaluation records. GreenTech Consortium must report accuracy and subgroup performance to ClinicalData Trust and erase evaluation outputs after 18 months.

1491. ConsumerResearch Agency may create synthetic data from the VoiceSample archive for model validation. Before release, ConsumerResearch Agency must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1492. HealthInsights Ltd may train an internal machine-learning model on the IncidentReports archive for fraud detection until 30 September 2026. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1493. AuditWorks must maintain version records for every model trained on the SupplierPerformance report, including provenance, training dates, intended purpose, and deletion status. Records must be retained for six months after model retirement.

1494. ResearchLab must not use the FraudSignals API to train a general-purpose AI model. Retrieval for academic research is permitted only within the European Economic Area, with prompts and outputs retained for no more than two years.

1495. AuditWorks may deploy a model trained on the VoiceSample archive for 18 months. A qualified human must review any output that materially affects a person, and AuditWorks must maintain a process for contesting erroneous outputs.

1496. ConsumerResearch Agency may create synthetic data from the CookieIdentifiers table for risk assessment. Before release, ConsumerResearch Agency must assess re-identification and membership-inference risk and must not release samples that reproduce source records.

1497. TransitAI may train an internal machine-learning model on the EnvironmentalReadings feed for public-interest research until 30 June 2027. The model must not be used to make solely automated decisions about individuals, and the training copy must be deleted after training.

1498. ServiceIntegrator must maintain version records for every model trained on the FraudSignals API, including provenance, training dates, intended purpose, and deletion status. Records must be retained for twelve months after model retirement.

1499. HealthInsights Ltd may fine-tune a model using the StudentProgress records only after removing direct identifiers and applying annual penetration testing. Model outputs must be tested for memorisation before deployment.

1500. FraudPrevention Team may fine-tune a model using the ResearchImages collection only after removing direct identifiers and applying multi-factor authentication. Model outputs must be tested for memorisation before deployment.

## 7. Sensitive-data and privacy-oriented restrictions

1501. FraudPrevention Team may use the OpenStatistics catalogue to produce cohort statistics where every cohort includes at least 18 people. Individual scores, singling out, and contact targeting are prohibited.

1502. CivicData Unit may review free-text fields in the FacialTemplate collection for statistical analysis only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1503. DataTrust Member must minimise each export of the CreditRisk model to fields necessary for epidemiological research. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1504. LocalAuthority may use the VulnerabilityFindings report for statistical analysis only after pseudonymisation. LocalAuthority must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 1 January 2029.

1505. UniversityNorth must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the RetailTransactions table. Aggregate analysis for cybersecurity monitoring is permitted if those inferences are not produced.

1506. ServiceIntegrator may use the VoiceSample archive to produce cohort statistics where every cohort includes at least 20 people. Individual scores, singling out, and contact targeting are prohibited.

1507. CivicData Unit must honour an approved objection by excluding the affected record from future processing of the SupplierPerformance report within 24 hours. The record may be retained only in a suppression list used to prevent re-entry.

1508. PartnerCo must honour an approved objection by excluding the affected record from future processing of the BuildingAccess logs within 48 hours. The record may be retained only in a suppression list used to prevent re-entry.

1509. MediaArchive may process records concerning minors in the ResearchImages collection solely for quality assurance. Profiling for advertising, behavioural manipulation, and disclosure to public repositories are prohibited.

1510. LocalAuthority may review free-text fields in the EmployeeSurvey dataset for model validation only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1511. EduPlatform must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the RetailTransactions table. Aggregate analysis for accessibility testing is permitted if those inferences are not produced.

1512. PublicHealth Institute must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the VulnerabilityFindings report. Aggregate analysis for statistical analysis is permitted if those inferences are not produced.

1513. DataTrust Member may use the CustomerAnalytics dataset to produce cohort statistics where every cohort includes at least 14 people. Individual scores, singling out, and contact targeting are prohibited.

1514. AnalyticsVendor must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ClinicalOutcomes extract. Aggregate analysis for academic research is permitted if those inferences are not produced.

1515. DataTrust Member must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ResearchImages collection. Aggregate analysis for environmental forecasting is permitted if those inferences are not produced.

1516. FinRisk Services may process records concerning minors in the LegalDocuments corpus solely for accessibility testing. Profiling for advertising, behavioural manipulation, and disclosure to unapproved subcontractors are prohibited.

1517. RegulatorySandbox Participant may use the VoiceSample archive for regulatory reporting only after pseudonymisation. RegulatorySandbox Participant must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 30 September 2026.

1518. AnalyticsVendor must not use the CreditRisk model for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 28 February 2027.

1519. AnalyticsVendor must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ClinicalOutcomes extract. Aggregate analysis for clinical evaluation is permitted if those inferences are not produced.

1520. FraudPrevention Team may process records concerning minors in the LegalDocuments corpus solely for customer-support improvement. Profiling for advertising, behavioural manipulation, and disclosure to commercial partners are prohibited.

1521. TransitAI may review free-text fields in the LegalDocuments corpus for quality assurance only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1522. HealthInsights Ltd may use the LocationInsights dataset to produce cohort statistics where every cohort includes at least 18 people. Individual scores, singling out, and contact targeting are prohibited.

1523. PartnerCo may review free-text fields in the LocationInsights dataset for quality assurance only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1524. AuditWorks must honour an approved objection by excluding the affected record from future processing of the IncidentReports archive within 48 hours. The record may be retained only in a suppression list used to prevent re-entry.

1525. CloudProcessor must not use the EnergyUsage records for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 November 2027.

1526. ModelOps Supplier may process records concerning minors in the IncidentReports archive solely for transport planning. Profiling for advertising, behavioural manipulation, and disclosure to third parties are prohibited.

1527. CivicData Unit must honour an approved objection by excluding the affected record from future processing of the OpenStatistics catalogue within 48 hours. The record may be retained only in a suppression list used to prevent re-entry.

1528. InsuranceAnalytics may use the EnvironmentalReadings feed for accessibility testing only after pseudonymisation. InsuranceAnalytics must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 December 2026.

1529. GreenTech Consortium must minimise each export of the StudentProgress records to fields necessary for clinical evaluation. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1530. ResearchLab must minimise each export of the FacialTemplate collection to fields necessary for bias and fairness evaluation. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1531. HealthInsights Ltd must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ElectionResearch dataset. Aggregate analysis for quality assurance is permitted if those inferences are not produced.

1532. CloudProcessor must not use the VoiceSample archive for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 1 January 2029.

1533. TransitAI may use the VulnerabilityFindings report to produce cohort statistics where every cohort includes at least 18 people. Individual scores, singling out, and contact targeting are prohibited.

1534. CivicData Unit must minimise each export of the DeviceTelemetry stream to fields necessary for model validation. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1535. RegulatorySandbox Participant may process the FraudSignals API for twelve months using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1536. ServiceIntegrator may review free-text fields in the CustomerSupport transcripts for transport planning only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1537. ServiceIntegrator may use the FacialTemplate collection for public-interest research only after pseudonymisation. ServiceIntegrator must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 28 February 2027.

1538. ResearchLab may process records concerning minors in the ClinicalOutcomes extract solely for clinical evaluation. Profiling for advertising, behavioural manipulation, and disclosure to overseas recipients are prohibited.

1539. DataTrust Member may link the MarketingSegments dataset to another dataset only with a project-specific linkage key issued by PublicBody. Identity resolution and enrichment from data-broker sources are prohibited.

1540. UniversityNorth may use the CreditRisk model to produce cohort statistics where every cohort includes at least 18 people. Individual scores, singling out, and contact targeting are prohibited.

1541. InsuranceAnalytics may use the FacialTemplate collection to produce cohort statistics where every cohort includes at least 12 people. Individual scores, singling out, and contact targeting are prohibited.

1542. EduPlatform may process the FraudSignals API for the project term using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1543. ModelOps Supplier may use the CreditRisk model to produce cohort statistics where every cohort includes at least 20 people. Individual scores, singling out, and contact targeting are prohibited.

1544. PublicHealth Institute must minimise each export of the TrafficSensor feed to fields necessary for transport planning. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1545. MediaArchive may use the ClinicalOutcomes extract for cybersecurity monitoring only after pseudonymisation. MediaArchive must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 March 2028.

1546. PartnerCo may process the PseudonymisedMobility dataset for 90 days using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1547. ModelOps Supplier may use the LegalDocuments corpus for regulatory reporting only after pseudonymisation. ModelOps Supplier must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 1 January 2029.

1548. ResearchLab may review free-text fields in the ProductReviews corpus for energy-efficiency analysis only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1549. RegulatorySandbox Participant may use the DeviceTelemetry stream for educational assessment only after pseudonymisation. RegulatorySandbox Participant must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 March 2028.

1550. MediaArchive may review free-text fields in the ResearchImages collection for public-interest research only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1551. BioStudy Group must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the MarketingSegments dataset. Aggregate analysis for public-interest research is permitted if those inferences are not produced.

1552. EduPlatform must not use the IncidentReports archive for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 August 2029.

1553. RetailMetrics PLC must honour an approved objection by excluding the affected record from future processing of the PseudonymisedMobility dataset within 48 hours. The record may be retained only in a suppression list used to prevent re-entry.

1554. AuditWorks must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the CookieIdentifiers table. Aggregate analysis for fraud detection is permitted if those inferences are not produced.

1555. TransitAI may use the StudentProgress records for service improvement only after pseudonymisation. TransitAI must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 28 February 2027.

1556. FraudPrevention Team may use the EnvironmentalReadings feed to produce cohort statistics where every cohort includes at least 22 people. Individual scores, singling out, and contact targeting are prohibited.

1557. AnalyticsVendor must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ClinicalOutcomes extract. Aggregate analysis for quality assurance is permitted if those inferences are not produced.

1558. AnalyticsVendor may review free-text fields in the RetailTransactions table for public-interest research only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1559. PublicHealth Institute must not use the EmployeeSurvey dataset for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 November 2027.

1560. InsuranceAnalytics may process the PublicHealth dashboard for the audit engagement using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1561. FinRisk Services may review free-text fields in the DeviceTelemetry stream for statistical analysis only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1562. CivicData Unit may link the ElectionResearch dataset to another dataset only with a project-specific linkage key issued by ArchiveOwner. Identity resolution and enrichment from data-broker sources are prohibited.

1563. OpenScience Centre must minimise each export of the StudentProgress records to fields necessary for risk assessment. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1564. ServiceIntegrator must not use the EmployeeSurvey dataset for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 May 2028.

1565. ConsumerResearch Agency must honour an approved objection by excluding the affected record from future processing of the ProductReviews corpus within 36 hours. The record may be retained only in a suppression list used to prevent re-entry.

1566. ResearchLab may process records concerning minors in the DeviceTelemetry stream solely for quality assurance. Profiling for advertising, behavioural manipulation, and disclosure to commercial partners are prohibited.

1567. HealthInsights Ltd may process records concerning minors in the FacialTemplate collection solely for statistical analysis. Profiling for advertising, behavioural manipulation, and disclosure to members outside the project team are prohibited.

1568. FraudPrevention Team may review free-text fields in the SupplierPerformance report for service improvement only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1569. DataTrust Member must minimise each export of the SupplierPerformance report to fields necessary for clinical evaluation. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1570. PartnerCo may use the ProductReviews corpus for fraud detection only after pseudonymisation. PartnerCo must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 15 March 2028.

1571. CloudProcessor must not use the TrafficSensor feed for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 September 2026.

1572. AnalyticsVendor may link the EnergyUsage records to another dataset only with a project-specific linkage key issued by SourceAgency. Identity resolution and enrichment from data-broker sources are prohibited.

1573. OpenScience Centre must not use the LocationInsights dataset for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 28 February 2027.

1574. ModelOps Supplier may process the ProductReviews corpus for 30 days using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1575. TransitAI may link the EnvironmentalReadings feed to another dataset only with a project-specific linkage key issued by ArchiveOwner. Identity resolution and enrichment from data-broker sources are prohibited.

1576. FraudPrevention Team may use the CustomerAnalytics dataset to produce cohort statistics where every cohort includes at least 18 people. Individual scores, singling out, and contact targeting are prohibited.

1577. ResearchLab may link the FacialTemplate collection to another dataset only with a project-specific linkage key issued by SourceAgency. Identity resolution and enrichment from data-broker sources are prohibited.

1578. PublicHealth Institute may use the SyntheticPopulation dataset for cybersecurity monitoring only after pseudonymisation. PublicHealth Institute must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 December 2026.

1579. PartnerCo must honour an approved objection by excluding the affected record from future processing of the EnvironmentalReadings feed within five working days. The record may be retained only in a suppression list used to prevent re-entry.

1580. ResearchLab may process the ClinicalOutcomes extract for 90 days using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1581. ServiceIntegrator may use the StudentProgress records to produce cohort statistics where every cohort includes at least 20 people. Individual scores, singling out, and contact targeting are prohibited.

1582. BioStudy Group must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the LocationInsights dataset. Aggregate analysis for epidemiological research is permitted if those inferences are not produced.

1583. PublicHealth Institute may link the IncidentReports archive to another dataset only with a project-specific linkage key issued by ClinicalData Trust. Identity resolution and enrichment from data-broker sources are prohibited.

1584. RetailMetrics PLC must honour an approved objection by excluding the affected record from future processing of the VoiceSample archive within 36 hours. The record may be retained only in a suppression list used to prevent re-entry.

1585. ConsumerResearch Agency may link the IncidentReports archive to another dataset only with a project-specific linkage key issued by PlatformOperator. Identity resolution and enrichment from data-broker sources are prohibited.

1586. PublicHealth Institute may process records concerning minors in the SupplierPerformance report solely for educational assessment. Profiling for advertising, behavioural manipulation, and disclosure to advertising networks are prohibited.

1587. PartnerCo must minimise each export of the FraudSignals API to fields necessary for educational assessment. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1588. HealthInsights Ltd must not use the GenomicVariants extract for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 April 2029.

1589. BioStudy Group may process the FacialTemplate collection for the project term using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1590. HealthInsights Ltd must not use the SupplierPerformance report for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 August 2029.

1591. ConsumerResearch Agency may use the CustomerAnalytics dataset for risk assessment only after pseudonymisation. ConsumerResearch Agency must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 August 2029.

1592. PublicHealth Institute may review free-text fields in the SyntheticPopulation dataset for statistical analysis only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1593. InsuranceAnalytics may use the CustomerSupport transcripts for regulatory reporting only after pseudonymisation. InsuranceAnalytics must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 30 June 2027.

1594. DataTrust Member may use the ResearchImages collection for cybersecurity monitoring only after pseudonymisation. DataTrust Member must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 28 February 2027.

1595. TransitAI may use the VulnerabilityFindings report for statistical analysis only after pseudonymisation. TransitAI must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 March 2028.

1596. ServiceIntegrator must not use the DeviceTelemetry stream for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 August 2029.

1597. RegulatorySandbox Participant must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ResearchImages collection. Aggregate analysis for quality assurance is permitted if those inferences are not produced.

1598. RegulatorySandbox Participant must honour an approved objection by excluding the affected record from future processing of the PublicHealth dashboard within 12 hours. The record may be retained only in a suppression list used to prevent re-entry.

1599. LocalAuthority must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ElectionResearch dataset. Aggregate analysis for service improvement is permitted if those inferences are not produced.

1600. DataTrust Member may process records concerning minors in the VulnerabilityFindings report solely for service improvement. Profiling for advertising, behavioural manipulation, and disclosure to advertising networks are prohibited.

1601. AnalyticsVendor may process the FraudSignals API for the audit engagement using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1602. GreenTech Consortium must not use the PseudonymisedMobility dataset for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 December 2026.

1603. DataTrust Member may review free-text fields in the ClinicalOutcomes extract for customer-support improvement only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1604. FraudPrevention Team may process records concerning minors in the ResearchImages collection solely for service improvement. Profiling for advertising, behavioural manipulation, and disclosure to unapproved subcontractors are prohibited.

1605. UniversityNorth may process records concerning minors in the CustomerAnalytics dataset solely for risk assessment. Profiling for advertising, behavioural manipulation, and disclosure to unauthorised affiliates are prohibited.

1606. FinRisk Services may use the MarketingSegments dataset to produce cohort statistics where every cohort includes at least 22 people. Individual scores, singling out, and contact targeting are prohibited.

1607. MediaArchive may process the VoiceSample archive for the audit engagement using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1608. FraudPrevention Team may review free-text fields in the EnvironmentalReadings feed for service improvement only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1609. DataTrust Member must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the PublicHealth dashboard. Aggregate analysis for contract performance monitoring is permitted if those inferences are not produced.

1610. DataTrust Member may use the MarketingSegments dataset to produce cohort statistics where every cohort includes at least 22 people. Individual scores, singling out, and contact targeting are prohibited.

1611. ModelOps Supplier may link the CustomerAnalytics dataset to another dataset only with a project-specific linkage key issued by PlatformOperator. Identity resolution and enrichment from data-broker sources are prohibited.

1612. PartnerCo may process the ProductReviews corpus for the pilot period using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1613. MediaArchive may process records concerning minors in the SyntheticPopulation dataset solely for energy-efficiency analysis. Profiling for advertising, behavioural manipulation, and disclosure to members outside the project team are prohibited.

1614. LocalAuthority may process records concerning minors in the DeviceTelemetry stream solely for regulatory reporting. Profiling for advertising, behavioural manipulation, and disclosure to overseas recipients are prohibited.

1615. BioStudy Group must minimise each export of the FraudSignals API to fields necessary for regulatory reporting. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1616. FraudPrevention Team may use the RetailTransactions table to produce cohort statistics where every cohort includes at least 12 people. Individual scores, singling out, and contact targeting are prohibited.

1617. TransitAI must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the OpenStatistics catalogue. Aggregate analysis for environmental forecasting is permitted if those inferences are not produced.

1618. AuditWorks must honour an approved objection by excluding the affected record from future processing of the CustomerSupport transcripts within 36 hours. The record may be retained only in a suppression list used to prevent re-entry.

1619. HealthInsights Ltd must not use the BuildingAccess logs for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 September 2026.

1620. ResearchLab may process records concerning minors in the RetailTransactions table solely for educational assessment. Profiling for advertising, behavioural manipulation, and disclosure to third parties are prohibited.

1621. UniversityNorth must not use the LocationInsights dataset for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 September 2026.

1622. EduPlatform may use the PublicHealth dashboard for cybersecurity monitoring only after pseudonymisation. EduPlatform must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 28 February 2027.

1623. ConsumerResearch Agency may process records concerning minors in the EmployeeSurvey dataset solely for statistical analysis. Profiling for advertising, behavioural manipulation, and disclosure to advertising networks are prohibited.

1624. EduPlatform may link the ElectionResearch dataset to another dataset only with a project-specific linkage key issued by DataOwner. Identity resolution and enrichment from data-broker sources are prohibited.

1625. PartnerCo must minimise each export of the VulnerabilityFindings report to fields necessary for customer-support improvement. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1626. HealthInsights Ltd must honour an approved objection by excluding the affected record from future processing of the StudentProgress records within 72 hours. The record may be retained only in a suppression list used to prevent re-entry.

1627. ResearchLab must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the RetailTransactions table. Aggregate analysis for cybersecurity monitoring is permitted if those inferences are not produced.

1628. ModelOps Supplier must minimise each export of the TrafficSensor feed to fields necessary for regulatory reporting. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1629. PartnerCo may review free-text fields in the CustomerSupport transcripts for regulatory reporting only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1630. RegulatorySandbox Participant must not use the TrafficSensor feed for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 May 2028.

1631. HealthInsights Ltd must minimise each export of the FacialTemplate collection to fields necessary for quality assurance. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1632. InsuranceAnalytics may use the OpenStatistics catalogue for contract performance monitoring only after pseudonymisation. InsuranceAnalytics must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 December 2026.

1633. AnalyticsVendor may review free-text fields in the BuildingAccess logs for clinical evaluation only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1634. TransitAI must honour an approved objection by excluding the affected record from future processing of the ProductReviews corpus within 36 hours. The record may be retained only in a suppression list used to prevent re-entry.

1635. HealthInsights Ltd must not use the ClinicalOutcomes extract for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 June 2027.

1636. ModelOps Supplier may process the StudentProgress records for the pilot period using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1637. ServiceIntegrator may process the LegalDocuments corpus for the audit engagement using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1638. OpenScience Centre must not use the FraudSignals API for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 March 2028.

1639. MediaArchive may process records concerning minors in the PublicHealth dashboard solely for bias and fairness evaluation. Profiling for advertising, behavioural manipulation, and disclosure to overseas recipients are prohibited.

1640. DataTrust Member may process the OpenStatistics catalogue for 60 days using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1641. AuditWorks may process the LocationInsights dataset for 60 days using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1642. UniversityNorth may use the TrafficSensor feed for statistical analysis only after pseudonymisation. UniversityNorth must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 October 2026.

1643. UniversityNorth may use the CustomerAnalytics dataset to produce cohort statistics where every cohort includes at least 16 people. Individual scores, singling out, and contact targeting are prohibited.

1644. MediaArchive must minimise each export of the LegalDocuments corpus to fields necessary for epidemiological research. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1645. MediaArchive must minimise each export of the CreditRisk model to fields necessary for transport planning. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1646. CloudProcessor may use the ElectionResearch dataset for epidemiological research only after pseudonymisation. CloudProcessor must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 December 2026.

1647. ServiceIntegrator may process the EnergyUsage records for the project term using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1648. UniversityNorth must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the SyntheticPopulation dataset. Aggregate analysis for model validation is permitted if those inferences are not produced.

1649. TransitAI must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the GenomicVariants extract. Aggregate analysis for model validation is permitted if those inferences are not produced.

1650. AnalyticsVendor must honour an approved objection by excluding the affected record from future processing of the LocationInsights dataset within 24 hours. The record may be retained only in a suppression list used to prevent re-entry.

1651. ResearchLab may review free-text fields in the ProductReviews corpus for cybersecurity monitoring only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1652. FraudPrevention Team may process the ProductReviews corpus for the pilot period using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1653. LocalAuthority may link the CustomerAnalytics dataset to another dataset only with a project-specific linkage key issued by ClinicalData Trust. Identity resolution and enrichment from data-broker sources are prohibited.

1654. CivicData Unit must honour an approved objection by excluding the affected record from future processing of the LegalDocuments corpus within five working days. The record may be retained only in a suppression list used to prevent re-entry.

1655. TransitAI may use the LegalDocuments corpus for risk assessment only after pseudonymisation. TransitAI must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 28 February 2027.

1656. TransitAI may review free-text fields in the EmployeeSurvey dataset for contract performance monitoring only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1657. UniversityNorth must not use the CookieIdentifiers table for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 June 2027.

1658. ModelOps Supplier must minimise each export of the OpenStatistics catalogue to fields necessary for academic research. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1659. RetailMetrics PLC may link the VoiceSample archive to another dataset only with a project-specific linkage key issued by ArchiveOwner. Identity resolution and enrichment from data-broker sources are prohibited.

1660. CloudProcessor must not use the ClinicalOutcomes extract for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 28 February 2027.

1661. CivicData Unit may process the BuildingAccess logs for 30 days using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1662. InsuranceAnalytics may use the FraudSignals API to produce cohort statistics where every cohort includes at least 18 people. Individual scores, singling out, and contact targeting are prohibited.

1663. RegulatorySandbox Participant may use the SupplierPerformance report to produce cohort statistics where every cohort includes at least 22 people. Individual scores, singling out, and contact targeting are prohibited.

1664. GreenTech Consortium may process the DeviceTelemetry stream for twelve months using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1665. RegulatorySandbox Participant must not use the OpenStatistics catalogue for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 December 2026.

1666. InsuranceAnalytics may review free-text fields in the IncidentReports archive for public-interest research only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1667. PublicHealth Institute must honour an approved objection by excluding the affected record from future processing of the IncidentReports archive within 12 hours. The record may be retained only in a suppression list used to prevent re-entry.

1668. InsuranceAnalytics must not use the VoiceSample archive for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 15 March 2028.

1669. DataTrust Member may use the LocationInsights dataset to produce cohort statistics where every cohort includes at least 20 people. Individual scores, singling out, and contact targeting are prohibited.

1670. InsuranceAnalytics may use the EnvironmentalReadings feed for statistical analysis only after pseudonymisation. InsuranceAnalytics must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 October 2026.

1671. MediaArchive must honour an approved objection by excluding the affected record from future processing of the TrafficSensor feed within 12 hours. The record may be retained only in a suppression list used to prevent re-entry.

1672. FraudPrevention Team must not use the PublicHealth dashboard for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 December 2026.

1673. DataTrust Member may link the FraudSignals API to another dataset only with a project-specific linkage key issued by ArchiveOwner. Identity resolution and enrichment from data-broker sources are prohibited.

1674. InsuranceAnalytics may use the IncidentReports archive to produce cohort statistics where every cohort includes at least 16 people. Individual scores, singling out, and contact targeting are prohibited.

1675. FinRisk Services may use the DeviceTelemetry stream to produce cohort statistics where every cohort includes at least 14 people. Individual scores, singling out, and contact targeting are prohibited.

1676. PartnerCo may link the ElectionResearch dataset to another dataset only with a project-specific linkage key issued by SourceAgency. Identity resolution and enrichment from data-broker sources are prohibited.

1677. PublicHealth Institute must honour an approved objection by excluding the affected record from future processing of the MarketingSegments dataset within 48 hours. The record may be retained only in a suppression list used to prevent re-entry.

1678. CivicData Unit may use the TrafficSensor feed for contract performance monitoring only after pseudonymisation. CivicData Unit must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 October 2026.

1679. GreenTech Consortium may process the EnvironmentalReadings feed for two years using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1680. GreenTech Consortium must minimise each export of the PseudonymisedMobility dataset to fields necessary for public-interest research. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1681. DataTrust Member may process the EmployeeSurvey dataset for 60 days using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1682. GreenTech Consortium must minimise each export of the VulnerabilityFindings report to fields necessary for statistical analysis. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1683. MediaArchive may link the PublicHealth dashboard to another dataset only with a project-specific linkage key issued by DataOwner. Identity resolution and enrichment from data-broker sources are prohibited.

1684. ModelOps Supplier must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ElectionResearch dataset. Aggregate analysis for service improvement is permitted if those inferences are not produced.

1685. FraudPrevention Team must not use the LocationInsights dataset for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 December 2026.

1686. ConsumerResearch Agency may use the CookieIdentifiers table to produce cohort statistics where every cohort includes at least 20 people. Individual scores, singling out, and contact targeting are prohibited.

1687. UniversityNorth may use the EmployeeSurvey dataset to produce cohort statistics where every cohort includes at least 14 people. Individual scores, singling out, and contact targeting are prohibited.

1688. CloudProcessor may use the LocationInsights dataset to produce cohort statistics where every cohort includes at least 22 people. Individual scores, singling out, and contact targeting are prohibited.

1689. ModelOps Supplier may review free-text fields in the RetailTransactions table for statistical analysis only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1690. ServiceIntegrator may use the BuildingAccess logs for academic research only after pseudonymisation. ServiceIntegrator must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 30 April 2029.

1691. PartnerCo may process the SupplierPerformance report for 18 months using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1692. ModelOps Supplier may use the TrafficSensor feed for epidemiological research only after pseudonymisation. ModelOps Supplier must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 15 March 2028.

1693. RegulatorySandbox Participant must honour an approved objection by excluding the affected record from future processing of the SupplierPerformance report within 12 hours. The record may be retained only in a suppression list used to prevent re-entry.

1694. MediaArchive must honour an approved objection by excluding the affected record from future processing of the EmployeeSurvey dataset within 36 hours. The record may be retained only in a suppression list used to prevent re-entry.

1695. AnalyticsVendor must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the OpenStatistics catalogue. Aggregate analysis for transport planning is permitted if those inferences are not produced.

1696. AuditWorks must minimise each export of the DeviceTelemetry stream to fields necessary for contract performance monitoring. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1697. FinRisk Services must minimise each export of the ProductReviews corpus to fields necessary for accessibility testing. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1698. EduPlatform must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the CookieIdentifiers table. Aggregate analysis for contract performance monitoring is permitted if those inferences are not produced.

1699. AuditWorks may process the LocationInsights dataset for the pilot period using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1700. ConsumerResearch Agency must honour an approved objection by excluding the affected record from future processing of the ClinicalOutcomes extract within 12 hours. The record may be retained only in a suppression list used to prevent re-entry.

1701. FraudPrevention Team may review free-text fields in the DeviceTelemetry stream for model validation only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1702. RegulatorySandbox Participant must not use the PublicHealth dashboard for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 December 2026.

1703. BioStudy Group must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the CookieIdentifiers table. Aggregate analysis for customer-support improvement is permitted if those inferences are not produced.

1704. ConsumerResearch Agency may link the EmployeeSurvey dataset to another dataset only with a project-specific linkage key issued by CityData Office. Identity resolution and enrichment from data-broker sources are prohibited.

1705. CloudProcessor may process records concerning minors in the LocationInsights dataset solely for fraud detection. Profiling for advertising, behavioural manipulation, and disclosure to data brokers are prohibited.

1706. FraudPrevention Team may process the IncidentReports archive for 18 months using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1707. GreenTech Consortium may use the SupplierPerformance report for clinical evaluation only after pseudonymisation. GreenTech Consortium must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 30 April 2029.

1708. AuditWorks may link the CookieIdentifiers table to another dataset only with a project-specific linkage key issued by PublicBody. Identity resolution and enrichment from data-broker sources are prohibited.

1709. MediaArchive may review free-text fields in the CustomerSupport transcripts for statistical analysis only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1710. FraudPrevention Team may process the VoiceSample archive for the audit engagement using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1711. ConsumerResearch Agency may use the CustomerSupport transcripts to produce cohort statistics where every cohort includes at least 18 people. Individual scores, singling out, and contact targeting are prohibited.

1712. AnalyticsVendor may process the ResearchImages collection for 30 days using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1713. DataTrust Member must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the PseudonymisedMobility dataset. Aggregate analysis for bias and fairness evaluation is permitted if those inferences are not produced.

1714. UniversityNorth must minimise each export of the GenomicVariants extract to fields necessary for transport planning. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1715. LocalAuthority must not use the EnergyUsage records for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 March 2028.

1716. TransitAI must honour an approved objection by excluding the affected record from future processing of the FraudSignals API within 12 hours. The record may be retained only in a suppression list used to prevent re-entry.

1717. ConsumerResearch Agency must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the MarketingSegments dataset. Aggregate analysis for epidemiological research is permitted if those inferences are not produced.

1718. PartnerCo may link the ElectionResearch dataset to another dataset only with a project-specific linkage key issued by RightsHolder. Identity resolution and enrichment from data-broker sources are prohibited.

1719. PartnerCo must not use the PseudonymisedMobility dataset for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 November 2027.

1720. CivicData Unit must minimise each export of the ProductReviews corpus to fields necessary for model validation. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1721. OpenScience Centre must not use the TrafficSensor feed for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 October 2026.

1722. BioStudy Group must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the DeviceTelemetry stream. Aggregate analysis for quality assurance is permitted if those inferences are not produced.

1723. AnalyticsVendor may use the VulnerabilityFindings report to produce cohort statistics where every cohort includes at least 14 people. Individual scores, singling out, and contact targeting are prohibited.

1724. PartnerCo may process the CookieIdentifiers table for six months using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1725. CivicData Unit may process records concerning minors in the OpenStatistics catalogue solely for environmental forecasting. Profiling for advertising, behavioural manipulation, and disclosure to overseas recipients are prohibited.

1726. UniversityNorth must honour an approved objection by excluding the affected record from future processing of the ProductReviews corpus within five working days. The record may be retained only in a suppression list used to prevent re-entry.

1727. ServiceIntegrator may use the RetailTransactions table for energy-efficiency analysis only after pseudonymisation. ServiceIntegrator must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 31 October 2026.

1728. FinRisk Services may process records concerning minors in the VulnerabilityFindings report solely for contract performance monitoring. Profiling for advertising, behavioural manipulation, and disclosure to public repositories are prohibited.

1729. ResearchLab may use the MarketingSegments dataset to produce cohort statistics where every cohort includes at least 14 people. Individual scores, singling out, and contact targeting are prohibited.

1730. AnalyticsVendor must not use the SyntheticPopulation dataset for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 April 2029.

1731. HealthInsights Ltd must not use the BuildingAccess logs for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 1 January 2029.

1732. RegulatorySandbox Participant may process the EnvironmentalReadings feed for the project term using a rotating pseudonym. Persistent cross-service tracking, reconstruction of identity, and use for direct marketing are prohibited.

1733. PartnerCo must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the VoiceSample archive. Aggregate analysis for educational assessment is permitted if those inferences are not produced.

1734. GreenTech Consortium must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the ResearchImages collection. Aggregate analysis for educational assessment is permitted if those inferences are not produced.

1735. ResearchLab may link the ElectionResearch dataset to another dataset only with a project-specific linkage key issued by SourceAgency. Identity resolution and enrichment from data-broker sources are prohibited.

1736. FinRisk Services may process records concerning minors in the LegalDocuments corpus solely for service improvement. Profiling for advertising, behavioural manipulation, and disclosure to advertising networks are prohibited.

1737. ServiceIntegrator may review free-text fields in the PublicHealth dashboard for transport planning only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1738. OpenScience Centre must honour an approved objection by excluding the affected record from future processing of the VulnerabilityFindings report within 36 hours. The record may be retained only in a suppression list used to prevent re-entry.

1739. LocalAuthority may link the ClinicalOutcomes extract to another dataset only with a project-specific linkage key issued by Dataset Steward. Identity resolution and enrichment from data-broker sources are prohibited.

1740. AnalyticsVendor must honour an approved objection by excluding the affected record from future processing of the CustomerAnalytics dataset within 72 hours. The record may be retained only in a suppression list used to prevent re-entry.

1741. BioStudy Group may link the RetailTransactions table to another dataset only with a project-specific linkage key issued by ClinicalData Trust. Identity resolution and enrichment from data-broker sources are prohibited.

1742. EduPlatform must minimise each export of the FacialTemplate collection to fields necessary for educational assessment. Optional fields, direct identifiers, and records outside the approved date range must be excluded.

1743. OpenScience Centre may link the LocationInsights dataset to another dataset only with a project-specific linkage key issued by DataOwner. Identity resolution and enrichment from data-broker sources are prohibited.

1744. InsuranceAnalytics may use the DeviceTelemetry stream for accessibility testing only after pseudonymisation. InsuranceAnalytics must keep the re-identification key under separate control, must not attempt re-identification, and must delete both components by 30 September 2026.

1745. ConsumerResearch Agency may review free-text fields in the ResearchImages collection for public-interest research only within a secure environment. Names, contact details, and unexpected sensitive information must be redacted before analysts receive access.

1746. BioStudy Group must not use the IncidentReports archive for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 31 May 2028.

1747. AnalyticsVendor must not infer health status, political opinions, religion, ethnicity, sexual orientation, or trade-union membership from the MarketingSegments dataset. Aggregate analysis for regulatory reporting is permitted if those inferences are not produced.

1748. ModelOps Supplier may process records concerning minors in the ElectionResearch dataset solely for contract performance monitoring. Profiling for advertising, behavioural manipulation, and disclosure to unapproved subcontractors are prohibited.

1749. InsuranceAnalytics must not use the CustomerSupport transcripts for facial recognition, emotion detection, or biometric categorisation. Quality testing unrelated to identifying people is permitted until 30 April 2029.

1750. ResearchLab may use the TrafficSensor feed to produce cohort statistics where every cohort includes at least 22 people. Individual scores, singling out, and contact targeting are prohibited.

## 8. Geographic, device, format, and technical constraints

1751. FraudPrevention Team may call the ClinicalOutcomes extract API no more than 2,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1752. CivicData Unit may export aggregate results from the secure environment in the European Economic Area. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1753. DataTrust Member may receive the RetailTransactions table in encrypted CSV format once per month until 30 November 2027. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1754. HealthInsights Ltd may access the FraudSignals API only from the United Kingdom for regulatory reporting. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1755. MediaArchive may receive the OpenStatistics catalogue in encrypted CSV format once per month until 31 May 2028. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1756. DataTrust Member may export aggregate results from the secure environment in Germany and France. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1757. DataTrust Member may create up to 5 encrypted development copies of the CustomerSupport transcripts. Each copy must contain synthetic identifiers, remain in the European Economic Area, and be destroyed before 30 November 2027.

1758. DataTrust Member may receive the FacialTemplate collection in encrypted CSV format once per month until 30 June 2027. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1759. FinRisk Services may modify the DeviceTelemetry stream to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1760. PartnerCo may modify the ProductReviews corpus to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1761. InsuranceAnalytics may cache responses from the MarketingSegments dataset for no longer than 60 days. The cache must use quarterly access reviews, must not be indexed by public search engines, and must be purged when access is revoked.

1762. FinRisk Services may store one working copy of the IncidentReports archive in the United Kingdom and the EEA. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from PublicBody.

1763. RegulatorySandbox Participant may call the GenomicVariants extract API no more than 6,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1764. UniversityNorth may stream the CreditRisk model into a monitoring system for academic research. The system may buffer no more than 48 hours of content and must automatically discard older events.

1765. OpenScience Centre may export aggregate results from the secure environment in the United Kingdom and the EEA. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1766. ModelOps Supplier may access the PublicHealth dashboard only from the organisation's secure research environment for cybersecurity monitoring. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1767. PublicHealth Institute may call the EnergyUsage records API no more than 1,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1768. HealthInsights Ltd may print up to 3 pages from the CookieIdentifiers table for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 60 days.

1769. AnalyticsVendor may store one working copy of the CustomerAnalytics dataset in the United Kingdom and the EEA. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from CityData Office.

1770. CloudProcessor may create up to 7 encrypted development copies of the DeviceTelemetry stream. Each copy must contain synthetic identifiers, remain in the named project workspace, and be destroyed before 31 October 2026.

1771. ServiceIntegrator may modify the ClinicalOutcomes extract to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1772. FinRisk Services may cache responses from the PseudonymisedMobility dataset for no longer than six months. The cache must use encryption at rest and in transit, must not be indexed by public search engines, and must be purged when access is revoked.

1773. EduPlatform may export aggregate results from the secure environment in the organisation's secure research environment. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1774. AuditWorks may cache responses from the LocationInsights dataset for no longer than twelve months. The cache must use device-level encryption, must not be indexed by public search engines, and must be purged when access is revoked.

1775. RetailMetrics PLC may create up to 11 encrypted development copies of the SupplierPerformance report. Each copy must contain synthetic identifiers, remain in the organisation's secure research environment, and be destroyed before 30 June 2027.

1776. ServiceIntegrator may stream the FraudSignals API into a monitoring system for quality assurance. The system may buffer no more than 144 hours of content and must automatically discard older events.

1777. TransitAI may access the SupplierPerformance report only from the named project workspace for fraud detection. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1778. HealthInsights Ltd may print up to 11 pages from the EnvironmentalReadings feed for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 60 days.

1779. UniversityNorth may export aggregate results from the secure environment in the United Kingdom. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1780. ServiceIntegrator may print up to 1 page from the IncidentReports archive for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within the audit engagement.

1781. CloudProcessor may store one working copy of the ElectionResearch dataset in the organisation's secure research environment. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ClinicalData Trust.

1782. PublicHealth Institute may receive the PseudonymisedMobility dataset in encrypted CSV format once per month until 31 August 2029. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1783. LocalAuthority may call the SyntheticPopulation dataset API no more than 2,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1784. AnalyticsVendor may call the CustomerAnalytics dataset API no more than 2,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1785. UniversityNorth may export aggregate results from the secure environment in the United Kingdom and the EEA. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1786. DataTrust Member may create up to 7 encrypted development copies of the PublicHealth dashboard. Each copy must contain synthetic identifiers, remain in the organisation's secure research environment, and be destroyed before 1 January 2029.

1787. ModelOps Supplier may cache responses from the ElectionResearch dataset for no longer than 18 months. The cache must use network segmentation, must not be indexed by public search engines, and must be purged when access is revoked.

1788. LocalAuthority may cache responses from the DeviceTelemetry stream for no longer than the pilot period. The cache must use annual penetration testing, must not be indexed by public search engines, and must be purged when access is revoked.

1789. CivicData Unit may store one working copy of the PseudonymisedMobility dataset in the United Kingdom and the EEA. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ClinicalData Trust.

1790. TransitAI may export aggregate results from the secure environment in Germany and France. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1791. AnalyticsVendor may access the StudentProgress records only from the Republic of Ireland for transport planning. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1792. BioStudy Group may call the GenomicVariants extract API no more than 3,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1793. PublicHealth Institute may export aggregate results from the secure environment in the controller's protected network. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1794. RetailMetrics PLC may print up to 9 pages from the BuildingAccess logs for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 90 days.

1795. PartnerCo may create up to 1 encrypted development copy of the OpenStatistics catalogue. Each copy must contain synthetic identifiers, remain in Germany and France, and be destroyed before 31 March 2028.

1796. ServiceIntegrator may export aggregate results from the secure environment in the Republic of Ireland. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1797. GreenTech Consortium may stream the EnergyUsage records into a monitoring system for regulatory reporting. The system may buffer no more than 144 hours of content and must automatically discard older events.

1798. CloudProcessor may stream the CreditRisk model into a monitoring system for statistical analysis. The system may buffer no more than 192 hours of content and must automatically discard older events.

1799. AnalyticsVendor may store one working copy of the FraudSignals API in approved EEA data centres. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from CityData Office.

1800. ResearchLab may stream the GenomicVariants extract into a monitoring system for educational assessment. The system may buffer no more than 48 hours of content and must automatically discard older events.

1801. FraudPrevention Team may cache responses from the ProductReviews corpus for no longer than 90 days. The cache must use device-level encryption, must not be indexed by public search engines, and must be purged when access is revoked.

1802. RegulatorySandbox Participant may create up to 3 encrypted development copies of the StudentProgress records. Each copy must contain synthetic identifiers, remain in Germany and France, and be destroyed before 30 November 2027.

1803. PublicHealth Institute may export aggregate results from the secure environment in approved EEA data centres. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1804. AuditWorks may access the CookieIdentifiers table only from the Republic of Ireland for educational assessment. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1805. MediaArchive may store one working copy of the TrafficSensor feed in the European Economic Area. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from PlatformOperator.

1806. PartnerCo may receive the ProductReviews corpus in encrypted CSV format once per month until 31 March 2028. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1807. BioStudy Group may modify the RetailTransactions table to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1808. LocalAuthority may create up to 1 encrypted development copy of the EnvironmentalReadings feed. Each copy must contain synthetic identifiers, remain in approved EEA data centres, and be destroyed before 30 November 2027.

1809. FinRisk Services may access the EnergyUsage records only from the Republic of Ireland for accessibility testing. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1810. EduPlatform may cache responses from the ClinicalOutcomes extract for no longer than the audit engagement. The cache must use device-level encryption, must not be indexed by public search engines, and must be purged when access is revoked.

1811. OpenScience Centre may create up to 1 encrypted development copy of the PseudonymisedMobility dataset. Each copy must contain synthetic identifiers, remain in the United Kingdom and the EEA, and be destroyed before 30 June 2027.

1812. ConsumerResearch Agency may store one working copy of the DeviceTelemetry stream in approved EEA data centres. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ClinicalData Trust.

1813. AuditWorks may call the GenomicVariants extract API no more than 5,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1814. DataTrust Member may stream the ElectionResearch dataset into a monitoring system for environmental forecasting. The system may buffer no more than 240 hours of content and must automatically discard older events.

1815. CivicData Unit may store one working copy of the PseudonymisedMobility dataset in the controller's protected network. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from DataOwner.

1816. LocalAuthority may cache responses from the IncidentReports archive for no longer than 60 days. The cache must use least-privilege access, must not be indexed by public search engines, and must be purged when access is revoked.

1817. ServiceIntegrator may access the IncidentReports archive only from the United Kingdom and the EEA for environmental forecasting. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1818. CloudProcessor may cache responses from the RetailTransactions table for no longer than 90 days. The cache must use multi-factor authentication, must not be indexed by public search engines, and must be purged when access is revoked.

1819. OpenScience Centre may create up to 3 encrypted development copies of the CreditRisk model. Each copy must contain synthetic identifiers, remain in the named project workspace, and be destroyed before 31 March 2028.

1820. HealthInsights Ltd may export aggregate results from the secure environment in the named project workspace. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1821. GreenTech Consortium may call the CreditRisk model API no more than 1,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1822. EduPlatform may store one working copy of the EmployeeSurvey dataset in the European Economic Area. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ArchiveOwner.

1823. DataTrust Member may receive the StudentProgress records in encrypted CSV format once per month until 28 February 2027. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1824. BioStudy Group may print up to 5 pages from the ResearchImages collection for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within the audit engagement.

1825. CloudProcessor may call the CreditRisk model API no more than 3,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1826. DataTrust Member may export aggregate results from the secure environment in the controller's protected network. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1827. GreenTech Consortium may create up to 11 encrypted development copies of the CreditRisk model. Each copy must contain synthetic identifiers, remain in the organisation's secure research environment, and be destroyed before 30 November 2027.

1828. PublicHealth Institute may cache responses from the LegalDocuments corpus for no longer than twelve months. The cache must use network segmentation, must not be indexed by public search engines, and must be purged when access is revoked.

1829. LocalAuthority may modify the EmployeeSurvey dataset to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1830. RetailMetrics PLC may store one working copy of the VoiceSample archive in the organisation's secure research environment. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ArchiveOwner.

1831. FinRisk Services may stream the ResearchImages collection into a monitoring system for model validation. The system may buffer no more than 192 hours of content and must automatically discard older events.

1832. LocalAuthority may create up to 11 encrypted development copies of the GenomicVariants extract. Each copy must contain synthetic identifiers, remain in the United Kingdom, and be destroyed before 31 May 2028.

1833. ConsumerResearch Agency may modify the SupplierPerformance report to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1834. CloudProcessor may receive the DeviceTelemetry stream in encrypted CSV format once per month until 31 December 2026. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1835. GreenTech Consortium may access the VoiceSample archive only from Germany and France for quality assurance. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1836. TransitAI may call the EnvironmentalReadings feed API no more than 5,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1837. RegulatorySandbox Participant may stream the ClinicalOutcomes extract into a monitoring system for bias and fairness evaluation. The system may buffer no more than 96 hours of content and must automatically discard older events.

1838. OpenScience Centre may cache responses from the DeviceTelemetry stream for no longer than 60 days. The cache must use network segmentation, must not be indexed by public search engines, and must be purged when access is revoked.

1839. OpenScience Centre may store one working copy of the DeviceTelemetry stream in the organisation's secure research environment. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from CityData Office.

1840. ServiceIntegrator may access the BuildingAccess logs only from the United Kingdom for clinical evaluation. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1841. PublicHealth Institute may cache responses from the ProductReviews corpus for no longer than 30 days. The cache must use network segmentation, must not be indexed by public search engines, and must be purged when access is revoked.

1842. FraudPrevention Team may call the RetailTransactions table API no more than 5,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1843. GreenTech Consortium may export aggregate results from the secure environment in the named project workspace. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1844. MediaArchive may export aggregate results from the secure environment in the controller's protected network. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1845. DataTrust Member may stream the StudentProgress records into a monitoring system for statistical analysis. The system may buffer no more than 48 hours of content and must automatically discard older events.

1846. RetailMetrics PLC may cache responses from the EnvironmentalReadings feed for no longer than twelve months. The cache must use annual penetration testing, must not be indexed by public search engines, and must be purged when access is revoked.

1847. ServiceIntegrator may cache responses from the PseudonymisedMobility dataset for no longer than the pilot period. The cache must use least-privilege access, must not be indexed by public search engines, and must be purged when access is revoked.

1848. RegulatorySandbox Participant may stream the FacialTemplate collection into a monitoring system for educational assessment. The system may buffer no more than 144 hours of content and must automatically discard older events.

1849. RetailMetrics PLC may receive the RetailTransactions table in encrypted CSV format once per month until 30 September 2026. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1850. RegulatorySandbox Participant may modify the EmployeeSurvey dataset to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1851. HealthInsights Ltd may call the EmployeeSurvey dataset API no more than 5,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1852. RegulatorySandbox Participant may print up to 5 pages from the SyntheticPopulation dataset for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within the pilot period.

1853. AuditWorks may modify the BuildingAccess logs to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1854. BioStudy Group may access the EmployeeSurvey dataset only from approved UK data centres for cybersecurity monitoring. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1855. PublicHealth Institute may cache responses from the IncidentReports archive for no longer than the audit engagement. The cache must use encryption at rest and in transit, must not be indexed by public search engines, and must be purged when access is revoked.

1856. InsuranceAnalytics may receive the EmployeeSurvey dataset in encrypted CSV format once per month until 30 November 2027. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1857. FraudPrevention Team may modify the PseudonymisedMobility dataset to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1858. MediaArchive may receive the FraudSignals API in encrypted CSV format once per month until 30 April 2029. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1859. RegulatorySandbox Participant may print up to 11 pages from the OpenStatistics catalogue for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 30 days.

1860. OpenScience Centre may access the FraudSignals API only from the organisation's secure research environment for epidemiological research. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1861. ModelOps Supplier may create up to 7 encrypted development copies of the SyntheticPopulation dataset. Each copy must contain synthetic identifiers, remain in the named project workspace, and be destroyed before 30 April 2029.

1862. ConsumerResearch Agency may modify the CookieIdentifiers table to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1863. InsuranceAnalytics may export aggregate results from the secure environment in approved EEA data centres. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1864. InsuranceAnalytics may call the IncidentReports archive API no more than 2,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1865. FinRisk Services may receive the PublicHealth dashboard in encrypted CSV format once per month until 30 September 2026. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1866. MediaArchive may call the TrafficSensor feed API no more than 1,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1867. CloudProcessor may call the StudentProgress records API no more than 5,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1868. ConsumerResearch Agency may export aggregate results from the secure environment in the United Kingdom and the EEA. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1869. OpenScience Centre may receive the EnvironmentalReadings feed in encrypted CSV format once per month until 31 August 2029. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1870. CivicData Unit may export aggregate results from the secure environment in the United Kingdom. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1871. ServiceIntegrator may print up to 7 pages from the ClinicalOutcomes extract for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within the project term.

1872. PartnerCo may stream the RetailTransactions table into a monitoring system for accessibility testing. The system may buffer no more than 96 hours of content and must automatically discard older events.

1873. PublicHealth Institute may create up to 1 encrypted development copy of the CustomerSupport transcripts. Each copy must contain synthetic identifiers, remain in approved UK data centres, and be destroyed before 30 June 2027.

1874. DataTrust Member may print up to 11 pages from the MarketingSegments dataset for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within two years.

1875. DataTrust Member may receive the CustomerSupport transcripts in encrypted CSV format once per month until 31 August 2029. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1876. PartnerCo may export aggregate results from the secure environment in the organisation's secure research environment. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1877. ModelOps Supplier may print up to 7 pages from the EnvironmentalReadings feed for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 90 days.

1878. PublicHealth Institute may export aggregate results from the secure environment in approved UK data centres. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1879. MediaArchive may modify the MarketingSegments dataset to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1880. DataTrust Member may print up to 5 pages from the VulnerabilityFindings report for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within the project term.

1881. FraudPrevention Team may cache responses from the SupplierPerformance report for no longer than the audit engagement. The cache must use role-based access controls, must not be indexed by public search engines, and must be purged when access is revoked.

1882. ModelOps Supplier may export aggregate results from the secure environment in the controller's protected network. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1883. OpenScience Centre may access the LocationInsights dataset only from the Republic of Ireland for contract performance monitoring. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1884. RegulatorySandbox Participant may modify the ResearchImages collection to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1885. UniversityNorth may create up to 9 encrypted development copies of the PseudonymisedMobility dataset. Each copy must contain synthetic identifiers, remain in the named project workspace, and be destroyed before 15 March 2028.

1886. ConsumerResearch Agency may export aggregate results from the secure environment in approved EEA data centres. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1887. DataTrust Member may call the TrafficSensor feed API no more than 1,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1888. ModelOps Supplier may modify the EnvironmentalReadings feed to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1889. LocalAuthority may modify the SupplierPerformance report to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1890. HealthInsights Ltd may access the LegalDocuments corpus only from approved EEA data centres for academic research. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1891. ModelOps Supplier may create up to 7 encrypted development copies of the DeviceTelemetry stream. Each copy must contain synthetic identifiers, remain in the European Economic Area, and be destroyed before 30 September 2026.

1892. GreenTech Consortium may store one working copy of the ProductReviews corpus in the controller's protected network. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from PlatformOperator.

1893. TransitAI may call the PublicHealth dashboard API no more than 5,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1894. BioStudy Group may access the PseudonymisedMobility dataset only from the named project workspace for environmental forecasting. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1895. ResearchLab may stream the ResearchImages collection into a monitoring system for customer-support improvement. The system may buffer no more than 240 hours of content and must automatically discard older events.

1896. PartnerCo may stream the ResearchImages collection into a monitoring system for educational assessment. The system may buffer no more than 192 hours of content and must automatically discard older events.

1897. CivicData Unit may create up to 11 encrypted development copies of the VulnerabilityFindings report. Each copy must contain synthetic identifiers, remain in the European Economic Area, and be destroyed before 31 May 2028.

1898. ConsumerResearch Agency may create up to 9 encrypted development copies of the PublicHealth dashboard. Each copy must contain synthetic identifiers, remain in the Republic of Ireland, and be destroyed before 31 August 2029.

1899. RetailMetrics PLC may stream the LegalDocuments corpus into a monitoring system for model validation. The system may buffer no more than 288 hours of content and must automatically discard older events.

1900. InsuranceAnalytics may receive the SyntheticPopulation dataset in encrypted CSV format once per month until 31 March 2028. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1901. FraudPrevention Team may call the BuildingAccess logs API no more than 2,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1902. InsuranceAnalytics may export aggregate results from the secure environment in Germany and France. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1903. TransitAI may store one working copy of the SyntheticPopulation dataset in the controller's protected network. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from DataOwner.

1904. PublicHealth Institute may receive the FacialTemplate collection in encrypted CSV format once per month until 1 January 2029. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1905. FinRisk Services may call the VoiceSample archive API no more than 6,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1906. FraudPrevention Team may store one working copy of the CookieIdentifiers table in the United Kingdom. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ArchiveOwner.

1907. FinRisk Services may create up to 9 encrypted development copies of the OpenStatistics catalogue. Each copy must contain synthetic identifiers, remain in the European Economic Area, and be destroyed before 28 February 2027.

1908. ModelOps Supplier may receive the ClinicalOutcomes extract in encrypted CSV format once per month until 30 April 2029. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1909. BioStudy Group may stream the StudentProgress records into a monitoring system for regulatory reporting. The system may buffer no more than 288 hours of content and must automatically discard older events.

1910. AnalyticsVendor may cache responses from the SyntheticPopulation dataset for no longer than two years. The cache must use multi-factor authentication, must not be indexed by public search engines, and must be purged when access is revoked.

1911. FinRisk Services may cache responses from the ElectionResearch dataset for no longer than 90 days. The cache must use role-based access controls, must not be indexed by public search engines, and must be purged when access is revoked.

1912. DataTrust Member may stream the StudentProgress records into a monitoring system for fraud detection. The system may buffer no more than 240 hours of content and must automatically discard older events.

1913. RetailMetrics PLC may store one working copy of the EnergyUsage records in approved EEA data centres. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from CityData Office.

1914. BioStudy Group may stream the VoiceSample archive into a monitoring system for regulatory reporting. The system may buffer no more than 144 hours of content and must automatically discard older events.

1915. CivicData Unit may store one working copy of the PseudonymisedMobility dataset in the United Kingdom. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ArchiveOwner.

1916. FinRisk Services may receive the LocationInsights dataset in encrypted CSV format once per month until 28 February 2027. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1917. CloudProcessor may store one working copy of the EmployeeSurvey dataset in the United Kingdom. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ClinicalData Trust.

1918. UniversityNorth may export aggregate results from the secure environment in the named project workspace. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1919. AnalyticsVendor may create up to 1 encrypted development copy of the LegalDocuments corpus. Each copy must contain synthetic identifiers, remain in approved UK data centres, and be destroyed before 30 November 2027.

1920. ServiceIntegrator may receive the SyntheticPopulation dataset in encrypted CSV format once per month until 31 March 2028. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1921. EduPlatform may access the PublicHealth dashboard only from approved UK data centres for fraud detection. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1922. TransitAI may print up to 7 pages from the CustomerSupport transcripts for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 60 days.

1923. RegulatorySandbox Participant may modify the GenomicVariants extract to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1924. GreenTech Consortium may modify the CustomerAnalytics dataset to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1925. EduPlatform may receive the SyntheticPopulation dataset in encrypted CSV format once per month until 30 November 2027. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1926. LocalAuthority may stream the EnvironmentalReadings feed into a monitoring system for cybersecurity monitoring. The system may buffer no more than 96 hours of content and must automatically discard older events.

1927. UniversityNorth may stream the VoiceSample archive into a monitoring system for energy-efficiency analysis. The system may buffer no more than 240 hours of content and must automatically discard older events.

1928. OpenScience Centre may call the StudentProgress records API no more than 4,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1929. FraudPrevention Team may create up to 1 encrypted development copy of the ProductReviews corpus. Each copy must contain synthetic identifiers, remain in the organisation's secure research environment, and be destroyed before 30 June 2027.

1930. AnalyticsVendor may stream the FacialTemplate collection into a monitoring system for energy-efficiency analysis. The system may buffer no more than 48 hours of content and must automatically discard older events.

1931. ResearchLab may call the VulnerabilityFindings report API no more than 3,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1932. EduPlatform may access the BuildingAccess logs only from the European Economic Area for academic research. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1933. RegulatorySandbox Participant may create up to 5 encrypted development copies of the SyntheticPopulation dataset. Each copy must contain synthetic identifiers, remain in the United Kingdom, and be destroyed before 31 August 2029.

1934. CloudProcessor may print up to 5 pages from the CreditRisk model for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 60 days.

1935. ConsumerResearch Agency may export aggregate results from the secure environment in approved UK data centres. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1936. CloudProcessor may access the FraudSignals API only from Germany and France for service improvement. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1937. FraudPrevention Team may stream the EnvironmentalReadings feed into a monitoring system for cybersecurity monitoring. The system may buffer no more than 48 hours of content and must automatically discard older events.

1938. DataTrust Member may export aggregate results from the secure environment in the United Kingdom. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1939. RegulatorySandbox Participant may receive the BuildingAccess logs in encrypted CSV format once per month until 28 February 2027. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1940. DataTrust Member may cache responses from the IncidentReports archive for no longer than 30 days. The cache must use quarterly access reviews, must not be indexed by public search engines, and must be purged when access is revoked.

1941. CivicData Unit may store one working copy of the RetailTransactions table in the organisation's secure research environment. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from SourceAgency.

1942. RegulatorySandbox Participant may print up to 3 pages from the VulnerabilityFindings report for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within the pilot period.

1943. OpenScience Centre may stream the PseudonymisedMobility dataset into a monitoring system for statistical analysis. The system may buffer no more than 144 hours of content and must automatically discard older events.

1944. MediaArchive may cache responses from the PseudonymisedMobility dataset for no longer than 30 days. The cache must use tamper-evident audit logs, must not be indexed by public search engines, and must be purged when access is revoked.

1945. HealthInsights Ltd may print up to 9 pages from the CustomerSupport transcripts for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within six months.

1946. InsuranceAnalytics may create up to 11 encrypted development copies of the BuildingAccess logs. Each copy must contain synthetic identifiers, remain in the controller's protected network, and be destroyed before 30 September 2026.

1947. ResearchLab may store one working copy of the LegalDocuments corpus in the United Kingdom and the EEA. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from PublicBody.

1948. PublicHealth Institute may print up to 11 pages from the ProductReviews corpus for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within the audit engagement.

1949. DataTrust Member may export aggregate results from the secure environment in approved EEA data centres. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1950. LocalAuthority may print up to 7 pages from the SupplierPerformance report for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within six months.

1951. FraudPrevention Team may receive the IncidentReports archive in encrypted CSV format once per month until 31 May 2028. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1952. CloudProcessor may export aggregate results from the secure environment in the Republic of Ireland. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1953. CloudProcessor may access the EmployeeSurvey dataset only from the European Economic Area for environmental forecasting. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1954. BioStudy Group may export aggregate results from the secure environment in the organisation's secure research environment. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1955. MediaArchive may store one working copy of the ElectionResearch dataset in the organisation's secure research environment. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from PublicBody.

1956. ConsumerResearch Agency may receive the ClinicalOutcomes extract in encrypted CSV format once per month until 31 December 2026. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1957. FinRisk Services may modify the FacialTemplate collection to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1958. PartnerCo may receive the FraudSignals API in encrypted CSV format once per month until 31 March 2028. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1959. FraudPrevention Team may receive the RetailTransactions table in encrypted CSV format once per month until 31 August 2029. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1960. LocalAuthority may receive the EnvironmentalReadings feed in encrypted CSV format once per month until 30 April 2029. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1961. UniversityNorth may stream the StudentProgress records into a monitoring system for cybersecurity monitoring. The system may buffer no more than 96 hours of content and must automatically discard older events.

1962. PartnerCo may stream the CustomerSupport transcripts into a monitoring system for service improvement. The system may buffer no more than 96 hours of content and must automatically discard older events.

1963. RetailMetrics PLC may export aggregate results from the secure environment in the named project workspace. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1964. ResearchLab may print up to 3 pages from the GenomicVariants extract for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 30 days.

1965. ConsumerResearch Agency may print up to 9 pages from the SyntheticPopulation dataset for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within six months.

1966. FraudPrevention Team may modify the StudentProgress records to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1967. ModelOps Supplier may access the RetailTransactions table only from approved UK data centres for risk assessment. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1968. GreenTech Consortium may export aggregate results from the secure environment in the controller's protected network. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1969. TransitAI may access the GenomicVariants extract only from the organisation's secure research environment for accessibility testing. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1970. AnalyticsVendor may create up to 5 encrypted development copies of the StudentProgress records. Each copy must contain synthetic identifiers, remain in approved EEA data centres, and be destroyed before 31 March 2028.

1971. LocalAuthority may access the SupplierPerformance report only from the Republic of Ireland for environmental forecasting. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1972. AnalyticsVendor may receive the CustomerAnalytics dataset in encrypted CSV format once per month until 30 June 2027. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1973. TransitAI may stream the SupplierPerformance report into a monitoring system for statistical analysis. The system may buffer no more than 48 hours of content and must automatically discard older events.

1974. OpenScience Centre may modify the ClinicalOutcomes extract to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1975. TransitAI may export aggregate results from the secure environment in the organisation's secure research environment. Exports must pass automated disclosure checks and manual approval; raw-row export is prohibited.

1976. BioStudy Group may stream the TrafficSensor feed into a monitoring system for educational assessment. The system may buffer no more than 144 hours of content and must automatically discard older events.

1977. HealthInsights Ltd may modify the EnergyUsage records to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1978. ServiceIntegrator may print up to 9 pages from the VulnerabilityFindings report for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within 90 days.

1979. RegulatorySandbox Participant may cache responses from the LegalDocuments corpus for no longer than the audit engagement. The cache must use tamper-evident audit logs, must not be indexed by public search engines, and must be purged when access is revoked.

1980. FinRisk Services may stream the VoiceSample archive into a monitoring system for service improvement. The system may buffer no more than 48 hours of content and must automatically discard older events.

1981. ResearchLab may call the StudentProgress records API no more than 6,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1982. CivicData Unit may stream the CreditRisk model into a monitoring system for academic research. The system may buffer no more than 240 hours of content and must automatically discard older events.

1983. CivicData Unit may call the PseudonymisedMobility dataset API no more than 3,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1984. UniversityNorth may cache responses from the CustomerSupport transcripts for no longer than the pilot period. The cache must use continuous security monitoring, must not be indexed by public search engines, and must be purged when access is revoked.

1985. ServiceIntegrator may access the SupplierPerformance report only from the European Economic Area for academic research. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1986. RegulatorySandbox Participant may stream the LegalDocuments corpus into a monitoring system for environmental forecasting. The system may buffer no more than 48 hours of content and must automatically discard older events.

1987. UniversityNorth may call the PublicHealth dashboard API no more than 3,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

1988. RetailMetrics PLC may modify the PublicHealth dashboard to correct formatting errors but must not alter substantive values. Every change must be logged with the original value, reason, author, and timestamp.

1989. AuditWorks may cache responses from the BuildingAccess logs for no longer than 90 days. The cache must use role-based access controls, must not be indexed by public search engines, and must be purged when access is revoked.

1990. BioStudy Group may receive the EmployeeSurvey dataset in encrypted CSV format once per month until 31 March 2028. Conversion to another format is allowed only if metadata and provenance fields are preserved.

1991. OpenScience Centre may create up to 1 encrypted development copy of the SupplierPerformance report. Each copy must contain synthetic identifiers, remain in the Republic of Ireland, and be destroyed before 31 December 2026.

1992. ServiceIntegrator may store one working copy of the ClinicalOutcomes extract in the named project workspace. Replication across additional regions, offline media, or unmanaged backup services requires prior approval from ArchiveOwner.

1993. HealthInsights Ltd may print up to 5 pages from the LocationInsights dataset for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within the audit engagement.

1994. FraudPrevention Team may cache responses from the EmployeeSurvey dataset for no longer than the audit engagement. The cache must use annual penetration testing, must not be indexed by public search engines, and must be purged when access is revoked.

1995. RegulatorySandbox Participant may cache responses from the SupplierPerformance report for no longer than twelve months. The cache must use quarterly access reviews, must not be indexed by public search engines, and must be purged when access is revoked.

1996. AuditWorks may access the FraudSignals API only from the organisation's secure research environment for public-interest research. Copying to personal devices, consumer file-sharing services, or locations outside the approved region is prohibited.

1997. GreenTech Consortium may stream the VoiceSample archive into a monitoring system for epidemiological research. The system may buffer no more than 144 hours of content and must automatically discard older events.

1998. InsuranceAnalytics may create up to 3 encrypted development copies of the CustomerAnalytics dataset. Each copy must contain synthetic identifiers, remain in the Republic of Ireland, and be destroyed before 15 March 2028.

1999. PartnerCo may print up to 3 pages from the SyntheticPopulation dataset for an approved audit. Each page must be numbered, stored in a locked cabinet, and shredded within six months.

2000. FraudPrevention Team may call the TrafficSensor feed API no more than 3,000 times each day. Automated scraping, credential sharing, and attempts to bypass rate limits are prohibited.

## 9. Audit, reporting, quality, and accountability duties

2001. TransitAI must verify the accuracy of the MarketingSegments dataset before relying on it for accessibility testing. Suspected material errors must be flagged to DataOwner within 24 hours, and affected processing must be paused.

2002. FraudPrevention Team must permit ClinicalData Trust to audit controls protecting the EmployeeSurvey dataset once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve FraudPrevention Team's confidential information.

2003. EduPlatform must notify ClinicalData Trust before materially changing the purpose, system, recipient group, or location associated with the OpenStatistics catalogue. The change may proceed only after written approval.

2004. AnalyticsVendor must verify the accuracy of the IncidentReports archive before relying on it for clinical evaluation. Suspected material errors must be flagged to PublicBody within 48 hours, and affected processing must be paused.

2005. ServiceIntegrator may correct incomplete metadata in the PublicHealth dashboard. It must retain the original metadata, document the evidence for each correction, and submit changes to RightsHolder for approval.

2006. RegulatorySandbox Participant must verify the accuracy of the BuildingAccess logs before relying on it for energy-efficiency analysis. Suspected material errors must be flagged to ResearchSponsor within 36 hours, and affected processing must be paused.

2007. GreenTech Consortium must maintain a register describing every processing operation performed on the StudentProgress records. The register must identify purpose, users, systems, recipients, retention, and safeguards for 60 days.

2008. FinRisk Services may rely on the MarketingSegments dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2009. ServiceIntegrator may correct incomplete metadata in the ClinicalOutcomes extract. It must retain the original metadata, document the evidence for each correction, and submit changes to ResearchSponsor for approval.

2010. HealthInsights Ltd must provide evidence of deletion, access review, and security testing for the CreditRisk model within 36 hours after a reasonable request from PublicBody. Evidence may be redacted to protect unrelated systems.

2011. OpenScience Centre may use the CookieIdentifiers table for energy-efficiency analysis provided it submits a usage report to ArchiveOwner every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2012. ModelOps Supplier may appoint an independent assessor to review use of the RetailTransactions table. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2013. PublicHealth Institute may use the FraudSignals API for service improvement provided it submits a usage report to CityData Office every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2014. LocalAuthority must provide evidence of deletion, access review, and security testing for the FraudSignals API within 72 hours after a reasonable request from CityData Office. Evidence may be redacted to protect unrelated systems.

2015. CloudProcessor must permit SourceAgency to audit controls protecting the RetailTransactions table once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve CloudProcessor's confidential information.

2016. CloudProcessor must verify the accuracy of the DeviceTelemetry stream before relying on it for energy-efficiency analysis. Suspected material errors must be flagged to ClinicalData Trust within 36 hours, and affected processing must be paused.

2017. GreenTech Consortium must permit CityData Office to audit controls protecting the OpenStatistics catalogue once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve GreenTech Consortium's confidential information.

2018. CivicData Unit must provide evidence of deletion, access review, and security testing for the VoiceSample archive within five working days after a reasonable request from Dataset Steward. Evidence may be redacted to protect unrelated systems.

2019. TransitAI must test a sample of 5% of records in the DeviceTelemetry stream for completeness each quarter. It must report error rates to ArchiveOwner and must not silently overwrite disputed values.

2020. InsuranceAnalytics may appoint an independent assessor to review use of the StudentProgress records. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2021. MediaArchive may rely on the CustomerAnalytics dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2022. PublicHealth Institute may use the ElectionResearch dataset for academic research provided it submits a usage report to CityData Office every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2023. CloudProcessor must verify the accuracy of the EnvironmentalReadings feed before relying on it for cybersecurity monitoring. Suspected material errors must be flagged to PlatformOperator within five working days, and affected processing must be paused.

2024. RetailMetrics PLC must maintain a register describing every processing operation performed on the MarketingSegments dataset. The register must identify purpose, users, systems, recipients, retention, and safeguards for two years.

2025. InsuranceAnalytics must provide evidence of deletion, access review, and security testing for the VulnerabilityFindings report within 24 hours after a reasonable request from DataOwner. Evidence may be redacted to protect unrelated systems.

2026. FraudPrevention Team may correct incomplete metadata in the LocationInsights dataset. It must retain the original metadata, document the evidence for each correction, and submit changes to SourceAgency for approval.

2027. ModelOps Supplier may use the FacialTemplate collection for fraud detection provided it submits a usage report to ResearchSponsor every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2028. MediaArchive must notify ResearchSponsor before materially changing the purpose, system, recipient group, or location associated with the PublicHealth dashboard. The change may proceed only after written approval.

2029. AuditWorks must provide evidence of deletion, access review, and security testing for the CustomerSupport transcripts within 24 hours after a reasonable request from PublicBody. Evidence may be redacted to protect unrelated systems.

2030. HealthInsights Ltd must notify ResearchSponsor before materially changing the purpose, system, recipient group, or location associated with the ClinicalOutcomes extract. The change may proceed only after written approval.

2031. PublicHealth Institute must maintain a register describing every processing operation performed on the LocationInsights dataset. The register must identify purpose, users, systems, recipients, retention, and safeguards for 18 months.

2032. RegulatorySandbox Participant must notify ClinicalData Trust before materially changing the purpose, system, recipient group, or location associated with the FacialTemplate collection. The change may proceed only after written approval.

2033. DataTrust Member must notify ResearchSponsor before materially changing the purpose, system, recipient group, or location associated with the ElectionResearch dataset. The change may proceed only after written approval.

2034. EduPlatform must notify CityData Office before materially changing the purpose, system, recipient group, or location associated with the ResearchImages collection. The change may proceed only after written approval.

2035. PublicHealth Institute must provide evidence of deletion, access review, and security testing for the FacialTemplate collection within 12 hours after a reasonable request from SourceAgency. Evidence may be redacted to protect unrelated systems.

2036. FinRisk Services must permit Dataset Steward to audit controls protecting the LocationInsights dataset once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve FinRisk Services's confidential information.

2037. CivicData Unit may use the EnvironmentalReadings feed for energy-efficiency analysis provided it submits a usage report to PublicBody every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2038. MediaArchive must notify CityData Office before materially changing the purpose, system, recipient group, or location associated with the ElectionResearch dataset. The change may proceed only after written approval.

2039. MediaArchive must notify PublicBody before materially changing the purpose, system, recipient group, or location associated with the CookieIdentifiers table. The change may proceed only after written approval.

2040. RetailMetrics PLC may rely on the RetailTransactions table for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2041. CloudProcessor must verify the accuracy of the EmployeeSurvey dataset before relying on it for quality assurance. Suspected material errors must be flagged to ClinicalData Trust within five working days, and affected processing must be paused.

2042. RetailMetrics PLC may rely on the CustomerSupport transcripts for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2043. GreenTech Consortium must permit ClinicalData Trust to audit controls protecting the GenomicVariants extract once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve GreenTech Consortium's confidential information.

2044. ServiceIntegrator must permit Dataset Steward to audit controls protecting the TrafficSensor feed once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve ServiceIntegrator's confidential information.

2045. OpenScience Centre must provide evidence of deletion, access review, and security testing for the MarketingSegments dataset within five working days after a reasonable request from PublicBody. Evidence may be redacted to protect unrelated systems.

2046. UniversityNorth may correct incomplete metadata in the FraudSignals API. It must retain the original metadata, document the evidence for each correction, and submit changes to ClinicalData Trust for approval.

2047. ModelOps Supplier may appoint an independent assessor to review use of the ElectionResearch dataset. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2048. TransitAI must verify the accuracy of the LegalDocuments corpus before relying on it for service improvement. Suspected material errors must be flagged to DataOwner within five working days, and affected processing must be paused.

2049. CloudProcessor must test a sample of 5% of records in the BuildingAccess logs for completeness each quarter. It must report error rates to ClinicalData Trust and must not silently overwrite disputed values.

2050. RegulatorySandbox Participant must maintain a register describing every processing operation performed on the MarketingSegments dataset. The register must identify purpose, users, systems, recipients, retention, and safeguards for 60 days.

2051. FinRisk Services may appoint an independent assessor to review use of the EnergyUsage records. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2052. TransitAI may correct incomplete metadata in the ElectionResearch dataset. It must retain the original metadata, document the evidence for each correction, and submit changes to PlatformOperator for approval.

2053. PartnerCo may correct incomplete metadata in the EmployeeSurvey dataset. It must retain the original metadata, document the evidence for each correction, and submit changes to PublicBody for approval.

2054. CloudProcessor may correct incomplete metadata in the FraudSignals API. It must retain the original metadata, document the evidence for each correction, and submit changes to PublicBody for approval.

2055. ResearchLab may appoint an independent assessor to review use of the DeviceTelemetry stream. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2056. ModelOps Supplier may appoint an independent assessor to review use of the CreditRisk model. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2057. OpenScience Centre may correct incomplete metadata in the CustomerSupport transcripts. It must retain the original metadata, document the evidence for each correction, and submit changes to ArchiveOwner for approval.

2058. TransitAI may correct incomplete metadata in the MarketingSegments dataset. It must retain the original metadata, document the evidence for each correction, and submit changes to ClinicalData Trust for approval.

2059. ResearchLab must verify the accuracy of the StudentProgress records before relying on it for risk assessment. Suspected material errors must be flagged to Dataset Steward within five working days, and affected processing must be paused.

2060. UniversityNorth must maintain a register describing every processing operation performed on the ResearchImages collection. The register must identify purpose, users, systems, recipients, retention, and safeguards for two years.

2061. TransitAI must test a sample of 1% of records in the FraudSignals API for completeness each quarter. It must report error rates to PlatformOperator and must not silently overwrite disputed values.

2062. ConsumerResearch Agency must maintain a register describing every processing operation performed on the CookieIdentifiers table. The register must identify purpose, users, systems, recipients, retention, and safeguards for the audit engagement.

2063. TransitAI must provide evidence of deletion, access review, and security testing for the ResearchImages collection within 12 hours after a reasonable request from ArchiveOwner. Evidence may be redacted to protect unrelated systems.

2064. ModelOps Supplier must verify the accuracy of the ElectionResearch dataset before relying on it for regulatory reporting. Suspected material errors must be flagged to ClinicalData Trust within 36 hours, and affected processing must be paused.

2065. HealthInsights Ltd must test a sample of 1% of records in the BuildingAccess logs for completeness each quarter. It must report error rates to RightsHolder and must not silently overwrite disputed values.

2066. ModelOps Supplier must maintain a register describing every processing operation performed on the SupplierPerformance report. The register must identify purpose, users, systems, recipients, retention, and safeguards for the audit engagement.

2067. MediaArchive must permit SourceAgency to audit controls protecting the DeviceTelemetry stream once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve MediaArchive's confidential information.

2068. LocalAuthority must notify Dataset Steward before materially changing the purpose, system, recipient group, or location associated with the VulnerabilityFindings report. The change may proceed only after written approval.

2069. DataTrust Member must provide evidence of deletion, access review, and security testing for the PseudonymisedMobility dataset within 24 hours after a reasonable request from SourceAgency. Evidence may be redacted to protect unrelated systems.

2070. AnalyticsVendor must notify PlatformOperator before materially changing the purpose, system, recipient group, or location associated with the CookieIdentifiers table. The change may proceed only after written approval.

2071. ResearchLab must notify RightsHolder before materially changing the purpose, system, recipient group, or location associated with the TrafficSensor feed. The change may proceed only after written approval.

2072. ServiceIntegrator must notify PublicBody before materially changing the purpose, system, recipient group, or location associated with the EnvironmentalReadings feed. The change may proceed only after written approval.

2073. CivicData Unit must permit RightsHolder to audit controls protecting the VoiceSample archive once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve CivicData Unit's confidential information.

2074. PartnerCo may use the TrafficSensor feed for environmental forecasting provided it submits a usage report to CityData Office every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2075. ServiceIntegrator must permit RightsHolder to audit controls protecting the VulnerabilityFindings report once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve ServiceIntegrator's confidential information.

2076. ModelOps Supplier may rely on the FraudSignals API for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2077. PartnerCo may appoint an independent assessor to review use of the EnvironmentalReadings feed. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2078. FraudPrevention Team may correct incomplete metadata in the MarketingSegments dataset. It must retain the original metadata, document the evidence for each correction, and submit changes to DataOwner for approval.

2079. InsuranceAnalytics may appoint an independent assessor to review use of the FraudSignals API. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2080. LocalAuthority must test a sample of 15% of records in the ResearchImages collection for completeness each quarter. It must report error rates to ArchiveOwner and must not silently overwrite disputed values.

2081. DataTrust Member must maintain a register describing every processing operation performed on the MarketingSegments dataset. The register must identify purpose, users, systems, recipients, retention, and safeguards for the project term.

2082. PublicHealth Institute must test a sample of 1% of records in the VulnerabilityFindings report for completeness each quarter. It must report error rates to ArchiveOwner and must not silently overwrite disputed values.

2083. OpenScience Centre may rely on the OpenStatistics catalogue for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2084. AuditWorks must maintain a register describing every processing operation performed on the PublicHealth dashboard. The register must identify purpose, users, systems, recipients, retention, and safeguards for the project term.

2085. DataTrust Member may rely on the OpenStatistics catalogue for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2086. UniversityNorth must verify the accuracy of the StudentProgress records before relying on it for transport planning. Suspected material errors must be flagged to ResearchSponsor within 72 hours, and affected processing must be paused.

2087. HealthInsights Ltd must maintain a register describing every processing operation performed on the TrafficSensor feed. The register must identify purpose, users, systems, recipients, retention, and safeguards for 90 days.

2088. PartnerCo may appoint an independent assessor to review use of the PublicHealth dashboard. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2089. PartnerCo must test a sample of 15% of records in the CustomerSupport transcripts for completeness each quarter. It must report error rates to SourceAgency and must not silently overwrite disputed values.

2090. UniversityNorth must notify PublicBody before materially changing the purpose, system, recipient group, or location associated with the MarketingSegments dataset. The change may proceed only after written approval.

2091. ModelOps Supplier must notify ClinicalData Trust before materially changing the purpose, system, recipient group, or location associated with the SyntheticPopulation dataset. The change may proceed only after written approval.

2092. ResearchLab must notify PublicBody before materially changing the purpose, system, recipient group, or location associated with the VoiceSample archive. The change may proceed only after written approval.

2093. GreenTech Consortium may appoint an independent assessor to review use of the FacialTemplate collection. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2094. PublicHealth Institute must permit ArchiveOwner to audit controls protecting the ClinicalOutcomes extract once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve PublicHealth Institute's confidential information.

2095. PartnerCo must notify ClinicalData Trust before materially changing the purpose, system, recipient group, or location associated with the CustomerAnalytics dataset. The change may proceed only after written approval.

2096. FraudPrevention Team may rely on the MarketingSegments dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2097. ResearchLab must verify the accuracy of the CustomerSupport transcripts before relying on it for academic research. Suspected material errors must be flagged to PlatformOperator within 24 hours, and affected processing must be paused.

2098. UniversityNorth may use the FraudSignals API for fraud detection provided it submits a usage report to Dataset Steward every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2099. FraudPrevention Team must provide evidence of deletion, access review, and security testing for the OpenStatistics catalogue within 48 hours after a reasonable request from ClinicalData Trust. Evidence may be redacted to protect unrelated systems.

2100. LocalAuthority must permit ResearchSponsor to audit controls protecting the ProductReviews corpus once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve LocalAuthority's confidential information.

2101. RetailMetrics PLC must notify ArchiveOwner before materially changing the purpose, system, recipient group, or location associated with the SyntheticPopulation dataset. The change may proceed only after written approval.

2102. RetailMetrics PLC must test a sample of 15% of records in the SyntheticPopulation dataset for completeness each quarter. It must report error rates to CityData Office and must not silently overwrite disputed values.

2103. AuditWorks must permit CityData Office to audit controls protecting the ResearchImages collection once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve AuditWorks's confidential information.

2104. HealthInsights Ltd must notify ClinicalData Trust before materially changing the purpose, system, recipient group, or location associated with the EnvironmentalReadings feed. The change may proceed only after written approval.

2105. MediaArchive may correct incomplete metadata in the ProductReviews corpus. It must retain the original metadata, document the evidence for each correction, and submit changes to CityData Office for approval.

2106. ModelOps Supplier must maintain a register describing every processing operation performed on the RetailTransactions table. The register must identify purpose, users, systems, recipients, retention, and safeguards for 18 months.

2107. LocalAuthority must permit SourceAgency to audit controls protecting the BuildingAccess logs once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve LocalAuthority's confidential information.

2108. RetailMetrics PLC may use the CustomerAnalytics dataset for model validation provided it submits a usage report to RightsHolder every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2109. AnalyticsVendor may correct incomplete metadata in the OpenStatistics catalogue. It must retain the original metadata, document the evidence for each correction, and submit changes to PlatformOperator for approval.

2110. BioStudy Group may use the RetailTransactions table for fraud detection provided it submits a usage report to PublicBody every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2111. GreenTech Consortium must verify the accuracy of the RetailTransactions table before relying on it for clinical evaluation. Suspected material errors must be flagged to PlatformOperator within 72 hours, and affected processing must be paused.

2112. ServiceIntegrator must verify the accuracy of the FacialTemplate collection before relying on it for fraud detection. Suspected material errors must be flagged to PublicBody within 72 hours, and affected processing must be paused.

2113. HealthInsights Ltd must test a sample of 15% of records in the FraudSignals API for completeness each quarter. It must report error rates to ResearchSponsor and must not silently overwrite disputed values.

2114. DataTrust Member must verify the accuracy of the GenomicVariants extract before relying on it for public-interest research. Suspected material errors must be flagged to RightsHolder within 72 hours, and affected processing must be paused.

2115. LocalAuthority may rely on the CookieIdentifiers table for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2116. InsuranceAnalytics must permit ResearchSponsor to audit controls protecting the BuildingAccess logs once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve InsuranceAnalytics's confidential information.

2117. ResearchLab may appoint an independent assessor to review use of the LocationInsights dataset. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2118. ConsumerResearch Agency must provide evidence of deletion, access review, and security testing for the RetailTransactions table within 48 hours after a reasonable request from DataOwner. Evidence may be redacted to protect unrelated systems.

2119. EduPlatform must verify the accuracy of the IncidentReports archive before relying on it for model validation. Suspected material errors must be flagged to ArchiveOwner within 24 hours, and affected processing must be paused.

2120. BioStudy Group must maintain a register describing every processing operation performed on the SupplierPerformance report. The register must identify purpose, users, systems, recipients, retention, and safeguards for two years.

2121. GreenTech Consortium must test a sample of 15% of records in the PseudonymisedMobility dataset for completeness each quarter. It must report error rates to RightsHolder and must not silently overwrite disputed values.

2122. TransitAI may use the LocationInsights dataset for fraud detection provided it submits a usage report to RightsHolder every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2123. ModelOps Supplier must test a sample of 1% of records in the DeviceTelemetry stream for completeness each quarter. It must report error rates to DataOwner and must not silently overwrite disputed values.

2124. FraudPrevention Team may appoint an independent assessor to review use of the VoiceSample archive. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2125. LocalAuthority may correct incomplete metadata in the LegalDocuments corpus. It must retain the original metadata, document the evidence for each correction, and submit changes to DataOwner for approval.

2126. GreenTech Consortium must maintain a register describing every processing operation performed on the ClinicalOutcomes extract. The register must identify purpose, users, systems, recipients, retention, and safeguards for 90 days.

2127. LocalAuthority must test a sample of 5% of records in the StudentProgress records for completeness each quarter. It must report error rates to RightsHolder and must not silently overwrite disputed values.

2128. ServiceIntegrator must provide evidence of deletion, access review, and security testing for the FraudSignals API within 48 hours after a reasonable request from Dataset Steward. Evidence may be redacted to protect unrelated systems.

2129. DataTrust Member may correct incomplete metadata in the VoiceSample archive. It must retain the original metadata, document the evidence for each correction, and submit changes to ResearchSponsor for approval.

2130. MediaArchive must notify DataOwner before materially changing the purpose, system, recipient group, or location associated with the GenomicVariants extract. The change may proceed only after written approval.

2131. BioStudy Group must maintain a register describing every processing operation performed on the PseudonymisedMobility dataset. The register must identify purpose, users, systems, recipients, retention, and safeguards for 90 days.

2132. FinRisk Services may use the OpenStatistics catalogue for environmental forecasting provided it submits a usage report to CityData Office every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2133. FinRisk Services must provide evidence of deletion, access review, and security testing for the FraudSignals API within 48 hours after a reasonable request from ResearchSponsor. Evidence may be redacted to protect unrelated systems.

2134. UniversityNorth must verify the accuracy of the SupplierPerformance report before relying on it for bias and fairness evaluation. Suspected material errors must be flagged to ArchiveOwner within 12 hours, and affected processing must be paused.

2135. PartnerCo must verify the accuracy of the SupplierPerformance report before relying on it for statistical analysis. Suspected material errors must be flagged to CityData Office within 24 hours, and affected processing must be paused.

2136. OpenScience Centre must verify the accuracy of the IncidentReports archive before relying on it for transport planning. Suspected material errors must be flagged to PublicBody within five working days, and affected processing must be paused.

2137. ResearchLab must provide evidence of deletion, access review, and security testing for the StudentProgress records within 48 hours after a reasonable request from RightsHolder. Evidence may be redacted to protect unrelated systems.

2138. FraudPrevention Team must provide evidence of deletion, access review, and security testing for the VoiceSample archive within 36 hours after a reasonable request from PublicBody. Evidence may be redacted to protect unrelated systems.

2139. OpenScience Centre must provide evidence of deletion, access review, and security testing for the CustomerSupport transcripts within 48 hours after a reasonable request from Dataset Steward. Evidence may be redacted to protect unrelated systems.

2140. RetailMetrics PLC may appoint an independent assessor to review use of the CookieIdentifiers table. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2141. AnalyticsVendor may use the PseudonymisedMobility dataset for accessibility testing provided it submits a usage report to DataOwner every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2142. ResearchLab may use the GenomicVariants extract for energy-efficiency analysis provided it submits a usage report to ArchiveOwner every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2143. FraudPrevention Team may use the EnergyUsage records for public-interest research provided it submits a usage report to Dataset Steward every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2144. RetailMetrics PLC must notify Dataset Steward before materially changing the purpose, system, recipient group, or location associated with the FacialTemplate collection. The change may proceed only after written approval.

2145. AuditWorks must provide evidence of deletion, access review, and security testing for the CustomerSupport transcripts within 24 hours after a reasonable request from ArchiveOwner. Evidence may be redacted to protect unrelated systems.

2146. PublicHealth Institute must maintain a register describing every processing operation performed on the GenomicVariants extract. The register must identify purpose, users, systems, recipients, retention, and safeguards for the project term.

2147. EduPlatform must maintain a register describing every processing operation performed on the CustomerSupport transcripts. The register must identify purpose, users, systems, recipients, retention, and safeguards for twelve months.

2148. CloudProcessor must notify Dataset Steward before materially changing the purpose, system, recipient group, or location associated with the BuildingAccess logs. The change may proceed only after written approval.

2149. MediaArchive must maintain a register describing every processing operation performed on the TrafficSensor feed. The register must identify purpose, users, systems, recipients, retention, and safeguards for six months.

2150. ServiceIntegrator must maintain a register describing every processing operation performed on the CustomerSupport transcripts. The register must identify purpose, users, systems, recipients, retention, and safeguards for 18 months.

2151. FraudPrevention Team may use the TrafficSensor feed for quality assurance provided it submits a usage report to ResearchSponsor every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2152. InsuranceAnalytics must verify the accuracy of the GenomicVariants extract before relying on it for bias and fairness evaluation. Suspected material errors must be flagged to DataOwner within 48 hours, and affected processing must be paused.

2153. RetailMetrics PLC must test a sample of 1% of records in the LegalDocuments corpus for completeness each quarter. It must report error rates to ArchiveOwner and must not silently overwrite disputed values.

2154. ResearchLab must provide evidence of deletion, access review, and security testing for the FraudSignals API within 12 hours after a reasonable request from ResearchSponsor. Evidence may be redacted to protect unrelated systems.

2155. InsuranceAnalytics must verify the accuracy of the SyntheticPopulation dataset before relying on it for fraud detection. Suspected material errors must be flagged to ClinicalData Trust within 12 hours, and affected processing must be paused.

2156. HealthInsights Ltd may correct incomplete metadata in the IncidentReports archive. It must retain the original metadata, document the evidence for each correction, and submit changes to CityData Office for approval.

2157. CloudProcessor must permit Dataset Steward to audit controls protecting the CustomerAnalytics dataset once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve CloudProcessor's confidential information.

2158. ResearchLab must maintain a register describing every processing operation performed on the BuildingAccess logs. The register must identify purpose, users, systems, recipients, retention, and safeguards for twelve months.

2159. ServiceIntegrator must maintain a register describing every processing operation performed on the CustomerSupport transcripts. The register must identify purpose, users, systems, recipients, retention, and safeguards for 90 days.

2160. CloudProcessor must test a sample of 5% of records in the CustomerSupport transcripts for completeness each quarter. It must report error rates to RightsHolder and must not silently overwrite disputed values.

2161. FinRisk Services may correct incomplete metadata in the TrafficSensor feed. It must retain the original metadata, document the evidence for each correction, and submit changes to ClinicalData Trust for approval.

2162. RegulatorySandbox Participant may use the EmployeeSurvey dataset for risk assessment provided it submits a usage report to PlatformOperator every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2163. BioStudy Group must test a sample of 1% of records in the OpenStatistics catalogue for completeness each quarter. It must report error rates to ClinicalData Trust and must not silently overwrite disputed values.

2164. GreenTech Consortium must verify the accuracy of the LocationInsights dataset before relying on it for customer-support improvement. Suspected material errors must be flagged to SourceAgency within 24 hours, and affected processing must be paused.

2165. ServiceIntegrator must verify the accuracy of the DeviceTelemetry stream before relying on it for risk assessment. Suspected material errors must be flagged to PublicBody within 72 hours, and affected processing must be paused.

2166. PublicHealth Institute must notify ArchiveOwner before materially changing the purpose, system, recipient group, or location associated with the PublicHealth dashboard. The change may proceed only after written approval.

2167. PartnerCo may rely on the OpenStatistics catalogue for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2168. MediaArchive must permit ArchiveOwner to audit controls protecting the StudentProgress records once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve MediaArchive's confidential information.

2169. ResearchLab must test a sample of 5% of records in the SupplierPerformance report for completeness each quarter. It must report error rates to PublicBody and must not silently overwrite disputed values.

2170. TransitAI must permit ResearchSponsor to audit controls protecting the PublicHealth dashboard once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve TransitAI's confidential information.

2171. ConsumerResearch Agency may correct incomplete metadata in the ProductReviews corpus. It must retain the original metadata, document the evidence for each correction, and submit changes to RightsHolder for approval.

2172. ModelOps Supplier must verify the accuracy of the CustomerSupport transcripts before relying on it for customer-support improvement. Suspected material errors must be flagged to ClinicalData Trust within 24 hours, and affected processing must be paused.

2173. ModelOps Supplier must maintain a register describing every processing operation performed on the FraudSignals API. The register must identify purpose, users, systems, recipients, retention, and safeguards for the audit engagement.

2174. ServiceIntegrator must test a sample of 5% of records in the CustomerSupport transcripts for completeness each quarter. It must report error rates to ResearchSponsor and must not silently overwrite disputed values.

2175. InsuranceAnalytics must maintain a register describing every processing operation performed on the StudentProgress records. The register must identify purpose, users, systems, recipients, retention, and safeguards for the audit engagement.

2176. LocalAuthority must provide evidence of deletion, access review, and security testing for the PublicHealth dashboard within 12 hours after a reasonable request from CityData Office. Evidence may be redacted to protect unrelated systems.

2177. OpenScience Centre must permit RightsHolder to audit controls protecting the CookieIdentifiers table once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve OpenScience Centre's confidential information.

2178. UniversityNorth may rely on the IncidentReports archive for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2179. MediaArchive may use the SupplierPerformance report for customer-support improvement provided it submits a usage report to RightsHolder every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2180. ConsumerResearch Agency must notify PlatformOperator before materially changing the purpose, system, recipient group, or location associated with the SupplierPerformance report. The change may proceed only after written approval.

2181. FraudPrevention Team must provide evidence of deletion, access review, and security testing for the BuildingAccess logs within 48 hours after a reasonable request from SourceAgency. Evidence may be redacted to protect unrelated systems.

2182. FinRisk Services may appoint an independent assessor to review use of the RetailTransactions table. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2183. GreenTech Consortium may use the GenomicVariants extract for cybersecurity monitoring provided it submits a usage report to DataOwner every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2184. FinRisk Services must verify the accuracy of the SupplierPerformance report before relying on it for environmental forecasting. Suspected material errors must be flagged to ResearchSponsor within 72 hours, and affected processing must be paused.

2185. CivicData Unit must verify the accuracy of the TrafficSensor feed before relying on it for cybersecurity monitoring. Suspected material errors must be flagged to RightsHolder within five working days, and affected processing must be paused.

2186. BioStudy Group may rely on the PublicHealth dashboard for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2187. CloudProcessor may correct incomplete metadata in the StudentProgress records. It must retain the original metadata, document the evidence for each correction, and submit changes to PublicBody for approval.

2188. PublicHealth Institute must provide evidence of deletion, access review, and security testing for the CookieIdentifiers table within five working days after a reasonable request from Dataset Steward. Evidence may be redacted to protect unrelated systems.

2189. HealthInsights Ltd must test a sample of 5% of records in the StudentProgress records for completeness each quarter. It must report error rates to PublicBody and must not silently overwrite disputed values.

2190. OpenScience Centre must permit ClinicalData Trust to audit controls protecting the EnvironmentalReadings feed once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve OpenScience Centre's confidential information.

2191. ModelOps Supplier may rely on the MarketingSegments dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2192. AuditWorks must notify PlatformOperator before materially changing the purpose, system, recipient group, or location associated with the CustomerSupport transcripts. The change may proceed only after written approval.

2193. AnalyticsVendor may rely on the RetailTransactions table for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2194. AnalyticsVendor must notify PlatformOperator before materially changing the purpose, system, recipient group, or location associated with the IncidentReports archive. The change may proceed only after written approval.

2195. LocalAuthority may use the PseudonymisedMobility dataset for epidemiological research provided it submits a usage report to PublicBody every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2196. CloudProcessor may rely on the CreditRisk model for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2197. OpenScience Centre must maintain a register describing every processing operation performed on the EnvironmentalReadings feed. The register must identify purpose, users, systems, recipients, retention, and safeguards for 18 months.

2198. CloudProcessor must test a sample of 5% of records in the PseudonymisedMobility dataset for completeness each quarter. It must report error rates to SourceAgency and must not silently overwrite disputed values.

2199. PartnerCo must provide evidence of deletion, access review, and security testing for the LocationInsights dataset within 72 hours after a reasonable request from ResearchSponsor. Evidence may be redacted to protect unrelated systems.

2200. AnalyticsVendor may use the CookieIdentifiers table for fraud detection provided it submits a usage report to PlatformOperator every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2201. CivicData Unit must test a sample of 5% of records in the TrafficSensor feed for completeness each quarter. It must report error rates to Dataset Steward and must not silently overwrite disputed values.

2202. FinRisk Services must verify the accuracy of the SyntheticPopulation dataset before relying on it for educational assessment. Suspected material errors must be flagged to PublicBody within 12 hours, and affected processing must be paused.

2203. FraudPrevention Team must test a sample of 15% of records in the PublicHealth dashboard for completeness each quarter. It must report error rates to DataOwner and must not silently overwrite disputed values.

2204. UniversityNorth must provide evidence of deletion, access review, and security testing for the ElectionResearch dataset within 24 hours after a reasonable request from ResearchSponsor. Evidence may be redacted to protect unrelated systems.

2205. RetailMetrics PLC must verify the accuracy of the IncidentReports archive before relying on it for public-interest research. Suspected material errors must be flagged to ClinicalData Trust within 72 hours, and affected processing must be paused.

2206. AuditWorks must provide evidence of deletion, access review, and security testing for the EnergyUsage records within 72 hours after a reasonable request from PlatformOperator. Evidence may be redacted to protect unrelated systems.

2207. CivicData Unit may rely on the PublicHealth dashboard for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2208. ServiceIntegrator may rely on the PseudonymisedMobility dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2209. ResearchLab may appoint an independent assessor to review use of the PublicHealth dashboard. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2210. ResearchLab may appoint an independent assessor to review use of the FacialTemplate collection. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2211. RetailMetrics PLC may use the LegalDocuments corpus for quality assurance provided it submits a usage report to Dataset Steward every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2212. MediaArchive must permit ResearchSponsor to audit controls protecting the CreditRisk model once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve MediaArchive's confidential information.

2213. CivicData Unit may rely on the EmployeeSurvey dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2214. InsuranceAnalytics may use the StudentProgress records for customer-support improvement provided it submits a usage report to ResearchSponsor every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2215. DataTrust Member must provide evidence of deletion, access review, and security testing for the CustomerAnalytics dataset within 72 hours after a reasonable request from ResearchSponsor. Evidence may be redacted to protect unrelated systems.

2216. FinRisk Services must permit DataOwner to audit controls protecting the MarketingSegments dataset once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve FinRisk Services's confidential information.

2217. ResearchLab must maintain a register describing every processing operation performed on the OpenStatistics catalogue. The register must identify purpose, users, systems, recipients, retention, and safeguards for 18 months.

2218. RetailMetrics PLC must test a sample of 1% of records in the ResearchImages collection for completeness each quarter. It must report error rates to SourceAgency and must not silently overwrite disputed values.

2219. ServiceIntegrator must maintain a register describing every processing operation performed on the VoiceSample archive. The register must identify purpose, users, systems, recipients, retention, and safeguards for 30 days.

2220. BioStudy Group may correct incomplete metadata in the ElectionResearch dataset. It must retain the original metadata, document the evidence for each correction, and submit changes to PlatformOperator for approval.

2221. CivicData Unit must permit ClinicalData Trust to audit controls protecting the ResearchImages collection once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve CivicData Unit's confidential information.

2222. HealthInsights Ltd may use the EnvironmentalReadings feed for statistical analysis provided it submits a usage report to ResearchSponsor every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2223. RegulatorySandbox Participant may appoint an independent assessor to review use of the ResearchImages collection. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2224. EduPlatform may correct incomplete metadata in the MarketingSegments dataset. It must retain the original metadata, document the evidence for each correction, and submit changes to PublicBody for approval.

2225. RegulatorySandbox Participant may appoint an independent assessor to review use of the SupplierPerformance report. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2226. ServiceIntegrator may appoint an independent assessor to review use of the SyntheticPopulation dataset. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2227. RegulatorySandbox Participant must provide evidence of deletion, access review, and security testing for the VoiceSample archive within five working days after a reasonable request from Dataset Steward. Evidence may be redacted to protect unrelated systems.

2228. DataTrust Member may appoint an independent assessor to review use of the VulnerabilityFindings report. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2229. RegulatorySandbox Participant may use the VulnerabilityFindings report for accessibility testing provided it submits a usage report to RightsHolder every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2230. BioStudy Group may appoint an independent assessor to review use of the VulnerabilityFindings report. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2231. ServiceIntegrator must verify the accuracy of the SupplierPerformance report before relying on it for educational assessment. Suspected material errors must be flagged to PublicBody within 12 hours, and affected processing must be paused.

2232. CloudProcessor may rely on the ElectionResearch dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2233. InsuranceAnalytics may correct incomplete metadata in the ClinicalOutcomes extract. It must retain the original metadata, document the evidence for each correction, and submit changes to PlatformOperator for approval.

2234. RegulatorySandbox Participant must permit Dataset Steward to audit controls protecting the VoiceSample archive once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve RegulatorySandbox Participant's confidential information.

2235. RetailMetrics PLC must permit PlatformOperator to audit controls protecting the ElectionResearch dataset once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve RetailMetrics PLC's confidential information.

2236. UniversityNorth must permit DataOwner to audit controls protecting the RetailTransactions table once per year on 20 working days' notice. The audit must avoid unrelated systems and preserve UniversityNorth's confidential information.

2237. RegulatorySandbox Participant may rely on the CustomerAnalytics dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2238. AnalyticsVendor must notify ResearchSponsor before materially changing the purpose, system, recipient group, or location associated with the ClinicalOutcomes extract. The change may proceed only after written approval.

2239. EduPlatform may correct incomplete metadata in the CustomerAnalytics dataset. It must retain the original metadata, document the evidence for each correction, and submit changes to PublicBody for approval.

2240. LocalAuthority may use the SyntheticPopulation dataset for educational assessment provided it submits a usage report to PublicBody every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2241. InsuranceAnalytics must maintain a register describing every processing operation performed on the BuildingAccess logs. The register must identify purpose, users, systems, recipients, retention, and safeguards for twelve months.

2242. FraudPrevention Team must provide evidence of deletion, access review, and security testing for the SupplierPerformance report within five working days after a reasonable request from PublicBody. Evidence may be redacted to protect unrelated systems.

2243. ModelOps Supplier must notify Dataset Steward before materially changing the purpose, system, recipient group, or location associated with the LegalDocuments corpus. The change may proceed only after written approval.

2244. AuditWorks may rely on the LocationInsights dataset for recommendations but must record material limitations and confidence levels. Unsupported certainty claims and concealment of known quality defects are prohibited.

2245. PartnerCo may use the MarketingSegments dataset for accessibility testing provided it submits a usage report to SourceAgency every quarter. The report must state users, purposes, exports, recipients, incidents, and deletion actions.

2246. PartnerCo may correct incomplete metadata in the StudentProgress records. It must retain the original metadata, document the evidence for each correction, and submit changes to ResearchSponsor for approval.

2247. RegulatorySandbox Participant may appoint an independent assessor to review use of the IncidentReports archive. The assessor may view necessary evidence but must not retain source records beyond the assessment.

2248. AuditWorks must verify the accuracy of the OpenStatistics catalogue before relying on it for transport planning. Suspected material errors must be flagged to ArchiveOwner within 36 hours, and affected processing must be paused.

2249. UniversityNorth may correct incomplete metadata in the PublicHealth dashboard. It must retain the original metadata, document the evidence for each correction, and submit changes to DataOwner for approval.

2250. PartnerCo must maintain a register describing every processing operation performed on the SupplierPerformance report. The register must identify purpose, users, systems, recipients, retention, and safeguards for two years.

## 10. Public-sector, archival, educational, and mixed scenarios

2251. PublicHealth Institute may preserve the TrafficSensor feed as an archival research record for the project term. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2252. RetailMetrics PLC may compare the FacialTemplate collection with public records for fraud detection. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2253. AnalyticsVendor may use the TrafficSensor feed during an emergency-response exercise lasting twelve months. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2254. AuditWorks may preserve the BuildingAccess logs as an archival research record for the project term. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2255. DataTrust Member may preserve the IncidentReports archive as an archival research record for 60 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2256. GreenTech Consortium may use the LegalDocuments corpus to prepare an official statistical release. Pre-release access is limited to 1 named staff member, and embargoed figures must not be disclosed before the announced publication time.

2257. HealthInsights Ltd may provide students with access to a de-identified subset of the StudentProgress records for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2258. RetailMetrics PLC may disclose the ElectionResearch dataset to a regulator acting within its authority. RetailMetrics PLC must record the legal basis, scope, recipient, and date, and must notify PublicBody unless notification is prohibited.

2259. RetailMetrics PLC may preserve the LocationInsights dataset as an archival research record for 18 months. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2260. PublicHealth Institute may use the BuildingAccess logs to prepare an official statistical release. Pre-release access is limited to 5 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2261. CloudProcessor may disclose the SupplierPerformance report to a regulator acting within its authority. CloudProcessor must record the legal basis, scope, recipient, and date, and must notify PublicBody unless notification is prohibited.

2262. ResearchLab may provide students with access to a de-identified subset of the VulnerabilityFindings report for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2263. PublicHealth Institute may preserve the SupplierPerformance report as an archival research record for the audit engagement. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2264. InsuranceAnalytics may preserve the SupplierPerformance report as an archival research record for 30 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2265. HealthInsights Ltd may use the CookieIdentifiers table for a public-sector pilot concerning regulatory reporting until 30 November 2027. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2266. OpenScience Centre may use the BuildingAccess logs during an emergency-response exercise lasting twelve months. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2267. TransitAI may preserve the MarketingSegments dataset as an archival research record for two years. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2268. LocalAuthority may translate descriptive fields in the BuildingAccess logs for bias and fairness evaluation. The translation must preserve meaning and provenance; original text must remain available for verification until 30 June 2027.

2269. ConsumerResearch Agency may use the CreditRisk model in a controlled policy simulation until 31 March 2028. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2270. FinRisk Services may use the ResearchImages collection for a public-sector pilot concerning energy-efficiency analysis until 28 February 2027. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2271. OpenScience Centre may use the ProductReviews corpus to prepare an official statistical release. Pre-release access is limited to 3 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2272. ConsumerResearch Agency may preserve the FraudSignals API as an archival research record for 30 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2273. ServiceIntegrator may use the VulnerabilityFindings report in a controlled policy simulation until 15 March 2028. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2274. ResearchLab may use the ProductReviews corpus to prepare an official statistical release. Pre-release access is limited to 7 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2275. TransitAI may use the CookieIdentifiers table for a public-sector pilot concerning energy-efficiency analysis until 30 April 2029. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2276. TransitAI may provide students with access to a de-identified subset of the ResearchImages collection for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2277. FinRisk Services may provide students with access to a de-identified subset of the CreditRisk model for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2278. OpenScience Centre may preserve the ResearchImages collection as an archival research record for 90 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2279. RegulatorySandbox Participant may use the IncidentReports archive for a public-sector pilot concerning accessibility testing until 30 September 2026. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2280. ResearchLab may translate descriptive fields in the FacialTemplate collection for academic research. The translation must preserve meaning and provenance; original text must remain available for verification until 28 February 2027.

2281. FraudPrevention Team may use the LocationInsights dataset for a public-sector pilot concerning bias and fairness evaluation until 30 April 2029. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2282. ResearchLab may provide students with access to a de-identified subset of the IncidentReports archive for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2283. AuditWorks may preserve the TrafficSensor feed as an archival research record for the pilot period. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2284. HealthInsights Ltd may disclose the DeviceTelemetry stream to a regulator acting within its authority. HealthInsights Ltd must record the legal basis, scope, recipient, and date, and must notify Dataset Steward unless notification is prohibited.

2285. LocalAuthority may preserve the MarketingSegments dataset as an archival research record for the audit engagement. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2286. EduPlatform may use the EnergyUsage records to prepare an official statistical release. Pre-release access is limited to 5 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2287. MediaArchive may create an accessible version of the IncidentReports archive for users with disabilities. Content changes must be limited to accessibility, attribution to SourceAgency must be preserved, and no additional personal data may be introduced.

2288. FinRisk Services may provide students with access to a de-identified subset of the GenomicVariants extract for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2289. CloudProcessor may use the SyntheticPopulation dataset for a public-sector pilot concerning statistical analysis until 31 March 2028. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2290. BioStudy Group may use the MarketingSegments dataset to prepare an official statistical release. Pre-release access is limited to 11 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2291. FinRisk Services may use the CreditRisk model in a controlled policy simulation until 31 August 2029. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2292. MediaArchive may disclose the CookieIdentifiers table to a regulator acting within its authority. MediaArchive must record the legal basis, scope, recipient, and date, and must notify SourceAgency unless notification is prohibited.

2293. LocalAuthority may preserve the TrafficSensor feed as an archival research record for twelve months. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2294. ResearchLab may disclose the StudentProgress records to a regulator acting within its authority. ResearchLab must record the legal basis, scope, recipient, and date, and must notify ArchiveOwner unless notification is prohibited.

2295. TransitAI may use the FacialTemplate collection in a controlled policy simulation until 31 August 2029. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2296. AnalyticsVendor may translate descriptive fields in the SyntheticPopulation dataset for model validation. The translation must preserve meaning and provenance; original text must remain available for verification until 15 March 2028.

2297. BioStudy Group may compare the OpenStatistics catalogue with public records for risk assessment. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2298. AuditWorks may provide students with access to a de-identified subset of the EmployeeSurvey dataset for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2299. RetailMetrics PLC may provide students with access to a de-identified subset of the MarketingSegments dataset for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2300. HealthInsights Ltd may use the IncidentReports archive for a public-sector pilot concerning cybersecurity monitoring until 31 August 2029. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2301. AnalyticsVendor may create an accessible version of the CreditRisk model for users with disabilities. Content changes must be limited to accessibility, attribution to RightsHolder must be preserved, and no additional personal data may be introduced.

2302. HealthInsights Ltd may provide students with access to a de-identified subset of the FacialTemplate collection for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2303. ModelOps Supplier may use the DeviceTelemetry stream in a controlled policy simulation until 31 October 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2304. DataTrust Member may use the CustomerAnalytics dataset to prepare an official statistical release. Pre-release access is limited to 5 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2305. CloudProcessor may disclose the ProductReviews corpus to a regulator acting within its authority. CloudProcessor must record the legal basis, scope, recipient, and date, and must notify Dataset Steward unless notification is prohibited.

2306. ConsumerResearch Agency may preserve the CustomerSupport transcripts as an archival research record for two years. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2307. CivicData Unit may preserve the LegalDocuments corpus as an archival research record for the audit engagement. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2308. LocalAuthority may preserve the VulnerabilityFindings report as an archival research record for the project term. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2309. ResearchLab may provide students with access to a de-identified subset of the FacialTemplate collection for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2310. MediaArchive may preserve the StudentProgress records as an archival research record for the project term. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2311. ResearchLab may preserve the EnergyUsage records as an archival research record for the pilot period. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2312. PartnerCo may compare the DeviceTelemetry stream with public records for public-interest research. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2313. OpenScience Centre may use the ResearchImages collection to prepare an official statistical release. Pre-release access is limited to 9 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2314. ModelOps Supplier may preserve the DeviceTelemetry stream as an archival research record for 60 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2315. GreenTech Consortium may translate descriptive fields in the DeviceTelemetry stream for clinical evaluation. The translation must preserve meaning and provenance; original text must remain available for verification until 30 November 2027.

2316. EduPlatform may use the DeviceTelemetry stream to prepare an official statistical release. Pre-release access is limited to 9 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2317. ConsumerResearch Agency may use the StudentProgress records during an emergency-response exercise lasting the pilot period. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2318. MediaArchive may use the GenomicVariants extract to prepare an official statistical release. Pre-release access is limited to 3 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2319. PartnerCo may provide students with access to a de-identified subset of the EnvironmentalReadings feed for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2320. ModelOps Supplier may provide students with access to a de-identified subset of the SyntheticPopulation dataset for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2321. CivicData Unit may preserve the EnvironmentalReadings feed as an archival research record for 60 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2322. ModelOps Supplier may use the IncidentReports archive for a public-sector pilot concerning cybersecurity monitoring until 30 November 2027. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2323. AnalyticsVendor may preserve the CookieIdentifiers table as an archival research record for the audit engagement. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2324. EduPlatform may preserve the RetailTransactions table as an archival research record for the pilot period. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2325. LocalAuthority may preserve the SyntheticPopulation dataset as an archival research record for six months. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2326. UniversityNorth may disclose the EnvironmentalReadings feed to a regulator acting within its authority. UniversityNorth must record the legal basis, scope, recipient, and date, and must notify PlatformOperator unless notification is prohibited.

2327. FinRisk Services may create an accessible version of the VoiceSample archive for users with disabilities. Content changes must be limited to accessibility, attribution to Dataset Steward must be preserved, and no additional personal data may be introduced.

2328. PublicHealth Institute may use the VulnerabilityFindings report during an emergency-response exercise lasting the project term. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2329. AuditWorks may use the VoiceSample archive for a public-sector pilot concerning transport planning until 31 May 2028. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2330. HealthInsights Ltd may use the FraudSignals API in a controlled policy simulation until 31 December 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2331. ServiceIntegrator may disclose the RetailTransactions table to a regulator acting within its authority. ServiceIntegrator must record the legal basis, scope, recipient, and date, and must notify DataOwner unless notification is prohibited.

2332. ResearchLab may disclose the LegalDocuments corpus to a regulator acting within its authority. ResearchLab must record the legal basis, scope, recipient, and date, and must notify DataOwner unless notification is prohibited.

2333. PublicHealth Institute may use the FraudSignals API during an emergency-response exercise lasting the pilot period. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2334. LocalAuthority may use the ProductReviews corpus to prepare an official statistical release. Pre-release access is limited to 3 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2335. ModelOps Supplier may use the CustomerSupport transcripts to prepare an official statistical release. Pre-release access is limited to 9 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2336. FinRisk Services may preserve the OpenStatistics catalogue as an archival research record for two years. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2337. EduPlatform may disclose the ResearchImages collection to a regulator acting within its authority. EduPlatform must record the legal basis, scope, recipient, and date, and must notify CityData Office unless notification is prohibited.

2338. ServiceIntegrator may use the EnergyUsage records during an emergency-response exercise lasting twelve months. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2339. AuditWorks may use the LegalDocuments corpus in a controlled policy simulation until 30 April 2029. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2340. ConsumerResearch Agency may preserve the ProductReviews corpus as an archival research record for the project term. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2341. ResearchLab may translate descriptive fields in the ResearchImages collection for environmental forecasting. The translation must preserve meaning and provenance; original text must remain available for verification until 31 August 2029.

2342. FraudPrevention Team may use the LegalDocuments corpus to prepare an official statistical release. Pre-release access is limited to 3 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2343. FinRisk Services may use the CustomerAnalytics dataset during an emergency-response exercise lasting 90 days. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2344. TransitAI may translate descriptive fields in the SupplierPerformance report for fraud detection. The translation must preserve meaning and provenance; original text must remain available for verification until 31 October 2026.

2345. HealthInsights Ltd may use the CustomerSupport transcripts in a controlled policy simulation until 30 September 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2346. InsuranceAnalytics may use the ResearchImages collection in a controlled policy simulation until 31 March 2028. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2347. GreenTech Consortium may disclose the BuildingAccess logs to a regulator acting within its authority. GreenTech Consortium must record the legal basis, scope, recipient, and date, and must notify DataOwner unless notification is prohibited.

2348. ResearchLab may use the OpenStatistics catalogue during an emergency-response exercise lasting the pilot period. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2349. FraudPrevention Team may use the EnergyUsage records in a controlled policy simulation until 31 October 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2350. ConsumerResearch Agency may use the ElectionResearch dataset for a public-sector pilot concerning customer-support improvement until 31 October 2026. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2351. AuditWorks may preserve the CustomerSupport transcripts as an archival research record for two years. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2352. FraudPrevention Team may use the StudentProgress records to prepare an official statistical release. Pre-release access is limited to 11 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2353. RegulatorySandbox Participant may use the CustomerAnalytics dataset for a public-sector pilot concerning accessibility testing until 31 October 2026. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2354. AnalyticsVendor may disclose the CustomerSupport transcripts to a regulator acting within its authority. AnalyticsVendor must record the legal basis, scope, recipient, and date, and must notify PublicBody unless notification is prohibited.

2355. RegulatorySandbox Participant may translate descriptive fields in the CustomerAnalytics dataset for transport planning. The translation must preserve meaning and provenance; original text must remain available for verification until 1 January 2029.

2356. RetailMetrics PLC may use the OpenStatistics catalogue in a controlled policy simulation until 1 January 2029. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2357. CloudProcessor may use the LegalDocuments corpus to prepare an official statistical release. Pre-release access is limited to 11 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2358. OpenScience Centre may create an accessible version of the SupplierPerformance report for users with disabilities. Content changes must be limited to accessibility, attribution to CityData Office must be preserved, and no additional personal data may be introduced.

2359. CivicData Unit may compare the OpenStatistics catalogue with public records for customer-support improvement. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2360. RegulatorySandbox Participant may translate descriptive fields in the GenomicVariants extract for quality assurance. The translation must preserve meaning and provenance; original text must remain available for verification until 28 February 2027.

2361. GreenTech Consortium may compare the CookieIdentifiers table with public records for educational assessment. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2362. BioStudy Group may use the EnvironmentalReadings feed in a controlled policy simulation until 30 June 2027. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2363. PartnerCo may disclose the LocationInsights dataset to a regulator acting within its authority. PartnerCo must record the legal basis, scope, recipient, and date, and must notify ClinicalData Trust unless notification is prohibited.

2364. ModelOps Supplier may use the ResearchImages collection for a public-sector pilot concerning fraud detection until 31 October 2026. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2365. BioStudy Group may provide students with access to a de-identified subset of the GenomicVariants extract for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2366. MediaArchive may use the PublicHealth dashboard for a public-sector pilot concerning cybersecurity monitoring until 31 May 2028. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2367. HealthInsights Ltd may use the EmployeeSurvey dataset for a public-sector pilot concerning bias and fairness evaluation until 28 February 2027. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2368. BioStudy Group may preserve the LocationInsights dataset as an archival research record for twelve months. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2369. ResearchLab may provide students with access to a de-identified subset of the CustomerAnalytics dataset for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2370. PublicHealth Institute may use the VulnerabilityFindings report to prepare an official statistical release. Pre-release access is limited to 7 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2371. LocalAuthority may use the DeviceTelemetry stream to prepare an official statistical release. Pre-release access is limited to 1 named staff member, and embargoed figures must not be disclosed before the announced publication time.

2372. AnalyticsVendor may use the TrafficSensor feed to prepare an official statistical release. Pre-release access is limited to 3 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2373. InsuranceAnalytics may create an accessible version of the TrafficSensor feed for users with disabilities. Content changes must be limited to accessibility, attribution to Dataset Steward must be preserved, and no additional personal data may be introduced.

2374. FraudPrevention Team may use the CustomerSupport transcripts during an emergency-response exercise lasting the audit engagement. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2375. BioStudy Group may compare the CookieIdentifiers table with public records for educational assessment. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2376. AuditWorks may translate descriptive fields in the LocationInsights dataset for statistical analysis. The translation must preserve meaning and provenance; original text must remain available for verification until 30 April 2029.

2377. EduPlatform may compare the RetailTransactions table with public records for clinical evaluation. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2378. MediaArchive may translate descriptive fields in the LocationInsights dataset for quality assurance. The translation must preserve meaning and provenance; original text must remain available for verification until 30 June 2027.

2379. FraudPrevention Team may translate descriptive fields in the EmployeeSurvey dataset for accessibility testing. The translation must preserve meaning and provenance; original text must remain available for verification until 31 March 2028.

2380. ConsumerResearch Agency may use the SupplierPerformance report in a controlled policy simulation until 28 February 2027. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2381. RetailMetrics PLC may create an accessible version of the ResearchImages collection for users with disabilities. Content changes must be limited to accessibility, attribution to PlatformOperator must be preserved, and no additional personal data may be introduced.

2382. RetailMetrics PLC may use the CreditRisk model for a public-sector pilot concerning environmental forecasting until 31 October 2026. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2383. MediaArchive may use the SupplierPerformance report for a public-sector pilot concerning model validation until 30 June 2027. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2384. EduPlatform may disclose the SupplierPerformance report to a regulator acting within its authority. EduPlatform must record the legal basis, scope, recipient, and date, and must notify Dataset Steward unless notification is prohibited.

2385. GreenTech Consortium may use the RetailTransactions table to prepare an official statistical release. Pre-release access is limited to 5 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2386. PublicHealth Institute may disclose the EnvironmentalReadings feed to a regulator acting within its authority. PublicHealth Institute must record the legal basis, scope, recipient, and date, and must notify PublicBody unless notification is prohibited.

2387. RetailMetrics PLC may use the EnergyUsage records to prepare an official statistical release. Pre-release access is limited to 11 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2388. EduPlatform may use the FacialTemplate collection in a controlled policy simulation until 30 June 2027. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2389. EduPlatform may preserve the CookieIdentifiers table as an archival research record for twelve months. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2390. RegulatorySandbox Participant may provide students with access to a de-identified subset of the BuildingAccess logs for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2391. LocalAuthority may use the SyntheticPopulation dataset during an emergency-response exercise lasting six months. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2392. PartnerCo may use the ClinicalOutcomes extract for a public-sector pilot concerning bias and fairness evaluation until 30 June 2027. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2393. RetailMetrics PLC may provide students with access to a de-identified subset of the LocationInsights dataset for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2394. ModelOps Supplier may disclose the CustomerSupport transcripts to a regulator acting within its authority. ModelOps Supplier must record the legal basis, scope, recipient, and date, and must notify DataOwner unless notification is prohibited.

2395. BioStudy Group may use the EmployeeSurvey dataset in a controlled policy simulation until 15 March 2028. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2396. LocalAuthority may provide students with access to a de-identified subset of the FacialTemplate collection for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2397. InsuranceAnalytics may translate descriptive fields in the OpenStatistics catalogue for bias and fairness evaluation. The translation must preserve meaning and provenance; original text must remain available for verification until 31 August 2029.

2398. ServiceIntegrator may create an accessible version of the ClinicalOutcomes extract for users with disabilities. Content changes must be limited to accessibility, attribution to RightsHolder must be preserved, and no additional personal data may be introduced.

2399. AnalyticsVendor may use the SupplierPerformance report for a public-sector pilot concerning service improvement until 31 August 2029. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2400. FraudPrevention Team may create an accessible version of the SupplierPerformance report for users with disabilities. Content changes must be limited to accessibility, attribution to PlatformOperator must be preserved, and no additional personal data may be introduced.

2401. ConsumerResearch Agency may create an accessible version of the DeviceTelemetry stream for users with disabilities. Content changes must be limited to accessibility, attribution to PlatformOperator must be preserved, and no additional personal data may be introduced.

2402. RegulatorySandbox Participant may provide students with access to a de-identified subset of the VoiceSample archive for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2403. TransitAI may use the PublicHealth dashboard in a controlled policy simulation until 31 December 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2404. ResearchLab may disclose the ElectionResearch dataset to a regulator acting within its authority. ResearchLab must record the legal basis, scope, recipient, and date, and must notify CityData Office unless notification is prohibited.

2405. RetailMetrics PLC may disclose the StudentProgress records to a regulator acting within its authority. RetailMetrics PLC must record the legal basis, scope, recipient, and date, and must notify PublicBody unless notification is prohibited.

2406. FinRisk Services may translate descriptive fields in the GenomicVariants extract for contract performance monitoring. The translation must preserve meaning and provenance; original text must remain available for verification until 30 September 2026.

2407. AnalyticsVendor may preserve the SyntheticPopulation dataset as an archival research record for 60 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2408. AnalyticsVendor may provide students with access to a de-identified subset of the IncidentReports archive for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2409. OpenScience Centre may preserve the ProductReviews corpus as an archival research record for twelve months. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2410. MediaArchive may use the StudentProgress records during an emergency-response exercise lasting 60 days. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2411. UniversityNorth may create an accessible version of the CustomerAnalytics dataset for users with disabilities. Content changes must be limited to accessibility, attribution to ClinicalData Trust must be preserved, and no additional personal data may be introduced.

2412. FinRisk Services may use the LegalDocuments corpus in a controlled policy simulation until 31 October 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2413. EduPlatform may use the VulnerabilityFindings report in a controlled policy simulation until 31 December 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2414. ServiceIntegrator may compare the VulnerabilityFindings report with public records for clinical evaluation. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2415. CivicData Unit may provide students with access to a de-identified subset of the CustomerAnalytics dataset for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2416. ConsumerResearch Agency may translate descriptive fields in the CreditRisk model for clinical evaluation. The translation must preserve meaning and provenance; original text must remain available for verification until 15 March 2028.

2417. PartnerCo may preserve the EmployeeSurvey dataset as an archival research record for 30 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2418. ConsumerResearch Agency may create an accessible version of the BuildingAccess logs for users with disabilities. Content changes must be limited to accessibility, attribution to SourceAgency must be preserved, and no additional personal data may be introduced.

2419. BioStudy Group may use the OpenStatistics catalogue for a public-sector pilot concerning academic research until 1 January 2029. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2420. EduPlatform may disclose the GenomicVariants extract to a regulator acting within its authority. EduPlatform must record the legal basis, scope, recipient, and date, and must notify DataOwner unless notification is prohibited.

2421. UniversityNorth may preserve the PseudonymisedMobility dataset as an archival research record for the project term. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2422. CivicData Unit may use the OpenStatistics catalogue for a public-sector pilot concerning fraud detection until 31 May 2028. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2423. RegulatorySandbox Participant may use the EnergyUsage records in a controlled policy simulation until 30 June 2027. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2424. CivicData Unit may use the BuildingAccess logs to prepare an official statistical release. Pre-release access is limited to 9 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2425. ConsumerResearch Agency may disclose the ElectionResearch dataset to a regulator acting within its authority. ConsumerResearch Agency must record the legal basis, scope, recipient, and date, and must notify SourceAgency unless notification is prohibited.

2426. ConsumerResearch Agency may provide students with access to a de-identified subset of the EnvironmentalReadings feed for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2427. UniversityNorth may disclose the FraudSignals API to a regulator acting within its authority. UniversityNorth must record the legal basis, scope, recipient, and date, and must notify Dataset Steward unless notification is prohibited.

2428. ResearchLab may preserve the IncidentReports archive as an archival research record for 30 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2429. MediaArchive may use the CustomerAnalytics dataset in a controlled policy simulation until 15 March 2028. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2430. CivicData Unit may use the EnvironmentalReadings feed to prepare an official statistical release. Pre-release access is limited to 11 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2431. HealthInsights Ltd may provide students with access to a de-identified subset of the ResearchImages collection for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2432. ConsumerResearch Agency may use the LocationInsights dataset for a public-sector pilot concerning public-interest research until 30 September 2026. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2433. PublicHealth Institute may provide students with access to a de-identified subset of the CustomerSupport transcripts for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2434. InsuranceAnalytics may translate descriptive fields in the FacialTemplate collection for environmental forecasting. The translation must preserve meaning and provenance; original text must remain available for verification until 15 March 2028.

2435. CloudProcessor may compare the CreditRisk model with public records for service improvement. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2436. InsuranceAnalytics may create an accessible version of the CustomerSupport transcripts for users with disabilities. Content changes must be limited to accessibility, attribution to ClinicalData Trust must be preserved, and no additional personal data may be introduced.

2437. ModelOps Supplier may use the StudentProgress records in a controlled policy simulation until 30 June 2027. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2438. HealthInsights Ltd may disclose the CookieIdentifiers table to a regulator acting within its authority. HealthInsights Ltd must record the legal basis, scope, recipient, and date, and must notify DataOwner unless notification is prohibited.

2439. PartnerCo may create an accessible version of the LegalDocuments corpus for users with disabilities. Content changes must be limited to accessibility, attribution to DataOwner must be preserved, and no additional personal data may be introduced.

2440. CivicData Unit may provide students with access to a de-identified subset of the EnvironmentalReadings feed for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2441. LocalAuthority may compare the TrafficSensor feed with public records for risk assessment. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2442. RetailMetrics PLC may use the ProductReviews corpus to prepare an official statistical release. Pre-release access is limited to 5 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2443. FinRisk Services may translate descriptive fields in the CustomerAnalytics dataset for statistical analysis. The translation must preserve meaning and provenance; original text must remain available for verification until 31 December 2026.

2444. FinRisk Services may use the EnvironmentalReadings feed for a public-sector pilot concerning environmental forecasting until 30 June 2027. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2445. DataTrust Member may disclose the IncidentReports archive to a regulator acting within its authority. DataTrust Member must record the legal basis, scope, recipient, and date, and must notify DataOwner unless notification is prohibited.

2446. PartnerCo may translate descriptive fields in the DeviceTelemetry stream for cybersecurity monitoring. The translation must preserve meaning and provenance; original text must remain available for verification until 30 November 2027.

2447. TransitAI may translate descriptive fields in the FraudSignals API for public-interest research. The translation must preserve meaning and provenance; original text must remain available for verification until 30 June 2027.

2448. CloudProcessor may use the VoiceSample archive to prepare an official statistical release. Pre-release access is limited to 3 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2449. RegulatorySandbox Participant may provide students with access to a de-identified subset of the CookieIdentifiers table for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2450. PublicHealth Institute may use the VulnerabilityFindings report to prepare an official statistical release. Pre-release access is limited to 5 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2451. ResearchLab may use the GenomicVariants extract for a public-sector pilot concerning quality assurance until 1 January 2029. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2452. InsuranceAnalytics may translate descriptive fields in the BuildingAccess logs for clinical evaluation. The translation must preserve meaning and provenance; original text must remain available for verification until 30 June 2027.

2453. LocalAuthority may disclose the CookieIdentifiers table to a regulator acting within its authority. LocalAuthority must record the legal basis, scope, recipient, and date, and must notify ResearchSponsor unless notification is prohibited.

2454. GreenTech Consortium may create an accessible version of the StudentProgress records for users with disabilities. Content changes must be limited to accessibility, attribution to PlatformOperator must be preserved, and no additional personal data may be introduced.

2455. RegulatorySandbox Participant may create an accessible version of the CookieIdentifiers table for users with disabilities. Content changes must be limited to accessibility, attribution to PlatformOperator must be preserved, and no additional personal data may be introduced.

2456. RegulatorySandbox Participant may provide students with access to a de-identified subset of the SyntheticPopulation dataset for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2457. ModelOps Supplier may use the SupplierPerformance report for a public-sector pilot concerning statistical analysis until 28 February 2027. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2458. InsuranceAnalytics may use the DeviceTelemetry stream in a controlled policy simulation until 31 October 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2459. ModelOps Supplier may translate descriptive fields in the EnvironmentalReadings feed for fraud detection. The translation must preserve meaning and provenance; original text must remain available for verification until 1 January 2029.

2460. EduPlatform may provide students with access to a de-identified subset of the ProductReviews corpus for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2461. CloudProcessor may use the StudentProgress records in a controlled policy simulation until 1 January 2029. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2462. CivicData Unit may use the ClinicalOutcomes extract in a controlled policy simulation until 1 January 2029. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2463. RegulatorySandbox Participant may preserve the SupplierPerformance report as an archival research record for the pilot period. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2464. TransitAI may disclose the GenomicVariants extract to a regulator acting within its authority. TransitAI must record the legal basis, scope, recipient, and date, and must notify RightsHolder unless notification is prohibited.

2465. AuditWorks may compare the RetailTransactions table with public records for public-interest research. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2466. ConsumerResearch Agency may create an accessible version of the PublicHealth dashboard for users with disabilities. Content changes must be limited to accessibility, attribution to PlatformOperator must be preserved, and no additional personal data may be introduced.

2467. GreenTech Consortium may translate descriptive fields in the VoiceSample archive for bias and fairness evaluation. The translation must preserve meaning and provenance; original text must remain available for verification until 31 May 2028.

2468. TransitAI may preserve the TrafficSensor feed as an archival research record for 60 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2469. CivicData Unit may provide students with access to a de-identified subset of the FacialTemplate collection for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2470. GreenTech Consortium may use the StudentProgress records in a controlled policy simulation until 31 May 2028. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2471. BioStudy Group may provide students with access to a de-identified subset of the BuildingAccess logs for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2472. OpenScience Centre may translate descriptive fields in the OpenStatistics catalogue for model validation. The translation must preserve meaning and provenance; original text must remain available for verification until 31 March 2028.

2473. ModelOps Supplier may use the RetailTransactions table for a public-sector pilot concerning statistical analysis until 30 September 2026. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2474. TransitAI may disclose the EnvironmentalReadings feed to a regulator acting within its authority. TransitAI must record the legal basis, scope, recipient, and date, and must notify ArchiveOwner unless notification is prohibited.

2475. UniversityNorth may compare the PseudonymisedMobility dataset with public records for academic research. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2476. RegulatorySandbox Participant may use the SyntheticPopulation dataset in a controlled policy simulation until 30 November 2027. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2477. AuditWorks may use the GenomicVariants extract during an emergency-response exercise lasting six months. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2478. OpenScience Centre may translate descriptive fields in the ResearchImages collection for educational assessment. The translation must preserve meaning and provenance; original text must remain available for verification until 30 April 2029.

2479. CloudProcessor may compare the TrafficSensor feed with public records for bias and fairness evaluation. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2480. RegulatorySandbox Participant may use the CustomerAnalytics dataset during an emergency-response exercise lasting the pilot period. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2481. CloudProcessor may preserve the ElectionResearch dataset as an archival research record for twelve months. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2482. RetailMetrics PLC may create an accessible version of the FraudSignals API for users with disabilities. Content changes must be limited to accessibility, attribution to PlatformOperator must be preserved, and no additional personal data may be introduced.

2483. HealthInsights Ltd may translate descriptive fields in the EnvironmentalReadings feed for public-interest research. The translation must preserve meaning and provenance; original text must remain available for verification until 31 December 2026.

2484. FraudPrevention Team may preserve the ResearchImages collection as an archival research record for six months. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2485. AuditWorks may translate descriptive fields in the EmployeeSurvey dataset for accessibility testing. The translation must preserve meaning and provenance; original text must remain available for verification until 31 March 2028.

2486. PartnerCo may use the RetailTransactions table to prepare an official statistical release. Pre-release access is limited to 7 named staff members, and embargoed figures must not be disclosed before the announced publication time.

2487. InsuranceAnalytics may preserve the CustomerAnalytics dataset as an archival research record for 90 days. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2488. FinRisk Services may preserve the VoiceSample archive as an archival research record for the project term. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.

2489. GreenTech Consortium may compare the SupplierPerformance report with public records for energy-efficiency analysis. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2490. FinRisk Services may provide students with access to a de-identified subset of the PublicHealth dashboard for one academic term. Students must accept confidentiality duties, and all course copies must be deleted after assessment.

2491. RegulatorySandbox Participant may create an accessible version of the DeviceTelemetry stream for users with disabilities. Content changes must be limited to accessibility, attribution to ResearchSponsor must be preserved, and no additional personal data may be introduced.

2492. EduPlatform may use the CookieIdentifiers table during an emergency-response exercise lasting 60 days. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2493. CloudProcessor may use the CreditRisk model for a public-sector pilot concerning regulatory reporting until 31 October 2026. Publication is limited to aggregated findings, and procurement or enforcement decisions must not rely solely on the pilot output.

2494. ModelOps Supplier may use the VoiceSample archive in a controlled policy simulation until 30 September 2026. Real-world intervention, individual targeting, and reuse for law-enforcement profiling are prohibited without a separate authorisation.

2495. OpenScience Centre may compare the SyntheticPopulation dataset with public records for statistical analysis. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2496. MediaArchive may use the VoiceSample archive to prepare an official statistical release. Pre-release access is limited to 1 named staff member, and embargoed figures must not be disclosed before the announced publication time.

2497. DataTrust Member may translate descriptive fields in the StudentProgress records for model validation. The translation must preserve meaning and provenance; original text must remain available for verification until 31 May 2028.

2498. RetailMetrics PLC may compare the CustomerAnalytics dataset with public records for transport planning. Matches must be treated as leads rather than facts, must undergo human verification, and must not be published at individual level.

2499. CloudProcessor may use the CustomerAnalytics dataset during an emergency-response exercise lasting the audit engagement. Operational deployment, unrelated surveillance, and retention after the exercise are prohibited.

2500. BioStudy Group may preserve the VulnerabilityFindings report as an archival research record for two years. Alteration of original records is prohibited; annotations must be stored separately and linked through stable archival references.
