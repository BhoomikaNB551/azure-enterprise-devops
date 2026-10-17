variable "subscription_id" {
  description = "Azure subscription ID"
  type        = string
  sensitive   = true
}

variable "location" {
  description = "Azure region for project resources"
  type        = string
  default     = "centralindia"
}

variable "resource_group_name" {
  description = "Azure resource group for the project"
  type        = string
  default     = "rg-enterprise-devops"
}
